from rest_framework import serializers
from .models import User, Team, Division,TeamInDivision, MatchTable,CourtSchedule

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'profilePic','email','password','phoneNumber')

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('teamName', 'captain', 'publicProfile','users')

class TeamInDivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamInDivision
        fields = ('division','team','position')

class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = ('name','admin','publicProfile')

class MatchTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchTable
        fields = ('id','team1Name','team2Name','ref','countDown','location','team1Wins','team2Wins')

class CourtScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourtSchedule
        fields = ('id','match','location','startTime','endTime','matchDetail')


    