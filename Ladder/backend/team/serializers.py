from rest_framework import serializers
from .models import *

class CreateTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name','captain')


class TeamSerializer(serializers.ModelSerializer):
    captain_username = serializers.SerializerMethodField()
    member_usernames = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = ('id', 'name','captain', 'users', 'captain_username', 'member_usernames')

    def get_captain_username(self, obj):
        return obj.captain.username

    def get_member_usernames(self, obj):
        return list(obj.users.values_list('username', flat=True))