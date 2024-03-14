from rest_framework import serializers
from .models import User, Team, Division,TeamInDivision

class TeamInDivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamInDivision
        fields = ('division','team','position')

class DivisionSerializer(serializers.ModelSerializer):
    admin_email = serializers.SerializerMethodField()
    
    class Meta:
        model = Division
        fields = ('name','admin','publicProfile', 'admin_email')

    def get_admin_email(self, obj):
        return obj.admin.email
    
        
