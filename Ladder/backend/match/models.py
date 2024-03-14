from django.db import models
from team.models import Team
from users.models import User

class MatchTable(models.Model):
    id = models.AutoField(primary_key=True)
    team1Name = models.ForeignKey(Team,related_name='team1_matches',on_delete=models.CASCADE)
    team2Name = models.ForeignKey(Team,related_name='team2_matches',on_delete=models.CASCADE)
    ref = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    countDown = models.DateField(null=True)
    team1Wins = models.IntegerField(default=0)
    team2Wins = models.IntegerField(default=0)
    class Status(models.TextChoices):
       INPROGRESS = 'i', 'inProgress'
       SCHEDULED = 's', 'scheduled'
       VOID = 'v', 'void'
       FINISHED = 'f', 'finished'
    status = models.CharField(max_length=1,choices=Status.choices,null=True)

#https://stackoverflow.com/questions/28712848/composite-primary-key-in-django
#make sure match always has a value
class CourtSchedule(models.Model):
    id = models.AutoField(primary_key=True)
    match = models.ForeignKey(MatchTable, on_delete=models.CASCADE, related_name='court_schedules', default=None)
    location = models.CharField(max_length=128)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    matchDetail = models.CharField(max_length=255,blank=True) 
