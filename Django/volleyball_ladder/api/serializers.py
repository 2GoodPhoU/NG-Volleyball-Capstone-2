from rest_framework import serializers
from .models import User, Team, Divisons, MatchTable,CourtSchedule

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'profilePic','email','password')

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('teamName', 'captain', 'publicProfile','users')

class DivisonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Divisons
        fields = ('id','teamName','publicProfile','position','admin')

class MatchTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchTable
        fields = ('id','team1Name','team2Name','ref','coutDown','location','team1Wins','team2Wins')

class CourtScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourtSchedule
        fields = ('location','id','startTime','endTime','matchDetail')


    