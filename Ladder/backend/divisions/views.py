from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status

from .models import Division,TeamInDivision, Team
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