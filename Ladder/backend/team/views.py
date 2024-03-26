from rest_framework import viewsets, permissions, status
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import action


# Create your views here.


class TeamViewset(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def list(self, request):
        queryset = Team.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CreateTeamSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()
            team_instance = serializer.save()  # Save the team instance
            team_instance.users.add(team_instance.captain)  # Add the captain to the users list
            print("Serialized Data:", serializer.data)

            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        project = self.queryset.get(pk=pk)
        serializer = self.serializer_class(project)
        return Response(serializer.data)


    def update(self, request, pk=None):
        project = self.queryset.get(pk=pk)
        serializer = self.serializer_class(project,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        project = self.queryset.get(pk=pk)
        project.delete()
        return Response(status=204)

    @action(detail=False, methods=['GET'], url_path='user_teams/(?P<user_id>\d+)')
    def user_teams(self, request, user_id=None):
        try:
            user_teams = Team.objects.filter(users=user_id)
            serializer = TeamSerializer(user_teams, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
    @action(detail=False, methods=['POST'], url_path='join_team/(?P<team_id>\d+)/(?P<user_id>\d+)')
    def join_team(self, request, team_id=None, user_id=None):
        try:
            team = Team.objects.get(pk=team_id)
            user = User.objects.get(pk=user_id)
            team.users.add(user)
            return Response({'message': f'User {user_id} joined team {team_id} successfully.'})
        except Team.DoesNotExist:
            return Response({'error': f'Team {team_id} does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
            return Response({'error': f'User {user_id} does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)