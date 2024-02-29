from django.shortcuts import render
from rest_framework import generics
from .models import User, Team, Divisons,MatchTable,CourtSchedule
from .serializers import UserSerializer,TeamSerializer,DivisonsSerializer
from .serializers import MatchTableSerializer,CourtScheduleSerializer
# Create your views here.

class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer