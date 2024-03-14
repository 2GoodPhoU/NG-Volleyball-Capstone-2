from django.db import models
from users.models import User
from team.models import Team

class Division(models.Model):
    name = models.CharField(max_length=55,primary_key=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    publicProfile = models.ImageField(upload_to='profile_images', blank= True, null=True)
    
    def __str__(self):
        return self.name
    
class TeamInDivision(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    position = models.PositiveIntegerField()
    class Meta:
        unique_together = ('division', 'team')