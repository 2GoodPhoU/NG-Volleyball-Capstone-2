from rest_framework import serializers
from .models import *

class MatchTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchTable
        fields = ('id','team1Name','team2Name','ref','coutDown','team1Wins','team2Wins','status')

class CourtScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourtSchedule
        fields = ('id','match','location','startTime','endTime','matchDetail')
