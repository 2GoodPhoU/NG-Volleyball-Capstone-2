from django.shortcuts import render
from rest_framework import generics
from .models import User, Team, Division,TeamInDivision,MatchTable,CourtSchedule
from .serializers import UserSerializer,TeamSerializer,DivisionSerializer,TeamInDivisionSerializer
from .serializers import MatchTableSerializer,CourtScheduleSerializer
# Create your views here.

class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamView(generics.CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class DivisionView(generics.CreateAPIView):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer

class MatchTableView(generics.CreateAPIView):
    queryset = MatchTable.objects.all()
    serializer_class = MatchTableSerializer

class CourtScheduleView(generics.CreateAPIView):
    queryset = CourtSchedule.objects.all()
    serializer_class = CourtScheduleSerializer

class TeamInDivisionView(generics.CreateAPIView):
    queryset = TeamInDivision.objects.all()
    serializer_class = TeamInDivisionSerializer