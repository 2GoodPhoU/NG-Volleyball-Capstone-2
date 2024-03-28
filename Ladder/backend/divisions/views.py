from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status

from django.db.models import Count,Sum,Case,When,FloatField, F
from .models import Division,TeamInDivision, Team, MatchTable
from .serializers import DivisionSerializer,TeamInDivisionSerializer
from rest_framework.decorators import action



class DivisionView(viewsets.ViewSet):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        queryset = Division.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
        
    def retrieve(self, request, pk=None):
        project = self.queryset.get(pk=pk)
        serializer = self.serializer_class(project)
        return Response(serializer.data)

class Tree:
    def __init__(self):
        self.positionNum = 0
        self.available = 0
        self.leafAmount = 1

    def get_win_rate(team_name):
        win_rate = MatchTable.objects.filter(
            status='f',#finished
            team1Name__teamName=team_name
        ).annotate(#adds addition field 'win'
            win=Case(
                When(team1Name__teamName=team_name, then=F('team1Wins')> F('team2Wins')),
                When(team2Name__teamName=team_name, then=F('team2Wins') > F('team1Wins')),
                default=0,
                output_field=FloatField()
            )
        ).aggregate(#calculations
            total_games=Count('id'),
            total_wins=Sum('win')
        )

        if win_rate['total_games'] == 0:#could be replaced with survay
            return 0.0  # Prevent division by zero

        return win_rate['total_wins'] / win_rate['total_games']

    #should work as passbyReference
    def assignPosition(self, team_list):
        # Reorganize the team list based on win rates
        team_list.sort(key=lambda team: self.get_win_rate(team.name))

        #assigning their positions
        for Team in team_list:
            if (self.available < self.leafAmount):
                Team.position = self.positionNum
                self.available += 1

            if (self.available == self.leafAmount):
                self.positionNum += 1
                self.available = 0
                self.leafAmount *= 2

        
class TeamInDivisionView(viewsets.ViewSet):
    queryset = TeamInDivision.objects.all()
    serializer_class = TeamInDivisionSerializer
    permission_classes = [permissions.AllowAny]


    def list(self, request):
        queryset = TeamInDivision.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
        
    def retrieve(self, request, pk=None):
        project = self.queryset.get(pk=pk)
        serializer = self.serializer_class(project)
        return Response(serializer.data)
    
    @action(detail=False, methods=['POST'], url_path=r'join_division/(?P<division_name>[^/.]+)/(?P<team_id>\d+)')
    def join_division(self, request, team_id, division_name):
        try:
            team = get_object_or_404(Team, id=team_id)
            division = get_object_or_404(Division, name=division_name)
            
            # Check if the team is already in the division
            if TeamInDivision.objects.filter(team=team, division=division).exists():
                return Response({'message': 'Team is already in the division'}, status=400)

            # Create a new TeamInDivision object to represent the relationship
            TeamInDivision.objects.create(team=team, division=division)
            
            return Response({'message': f'Team {team_id} joined division {division_name} successfully.'})
        except Team.DoesNotExist:
            return Response({'error': f'Team {team_id} does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        except Division.DoesNotExist:
            return Response({'error': f'Division {division_name} does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_queryset(self):
        division_name = self.kwargs['division_name']
        # Retrieve the division object by name
        division = get_object_or_404(Division, name=division_name)
        # Get all team-in-division objects for the division
        queryset = TeamInDivision.objects.filter(division=division)
        return queryset

    @action(detail=False, methods=['GET'], url_path=r'(?P<division_name>[^/.]+)')
    def list_by_division(self, request, division_name=None):
        division = get_object_or_404(Division, name=division_name)
        team_in_division = self.queryset.filter(division=division)
        serializer = self.serializer_class(team_in_division, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['POST'], url_path='assign-positions/(?P<division_name>[^/.]+)')
    def assign_positions(self, request, division_name=None):
        division = get_object_or_404(Division, name=division_name)
        TeamList = list(TeamInDivision.objects.filter(division=division))#querrySet into list
        tree = Tree()
        
        tree.assignPosition(TeamList)
        for team in TeamList #saves each teamObject to the database
            team.save()

        return Response({'message': 'Positions assigned successfully.'})