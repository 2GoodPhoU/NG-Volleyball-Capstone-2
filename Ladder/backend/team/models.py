from django.db import models
from users.models import User
# Create your models here.
class Team(models.Model):
    name = models.CharField(unique=True, max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    captain = models.ForeignKey(User,related_name='team_captain',on_delete=models.CASCADE)
    users = models.ManyToManyField(User,related_name='team_player')#teamPlayer table

    def __str__(self):
        return self.name