from django.db import models



#--------------note-------------------------------
#need to go bakc  and check: password authentification
#checked: if not nulls, many to many,delete cascade
#Need to test

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=55)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=128)
    profilePic = models.ImageField(null=True)

class Team(models.Model):
    teamName = models.CharField(max_length=55,primary_key=True)
    captain = models.ForeignKey(User,related_name='team_captain',on_delete=models.CASCADE)
    publicProfile = models.ImageField(null=True)
    users = models.ManyToManyField(User,related_name='team_player')#teamPlayer table

class Divisons(models.Model):
    id = models.AutoField(primary_key=True)
    teamName = models.ForeignKey(Team,on_delete=models.CASCADE)
    publicProfile = models.ImageField(null=True)
    position = models.IntegerField()
    admin = models.ForeignKey(User,on_delete=models.CASCADE)

class MatchTable(models.Model):
    id = models.AutoField(primary_key=True)
    team1Name = models.ForeignKey(Team,related_name='team1_matches',on_delete=models.CASCADE)
    team2Name = models.ForeignKey(Team,related_name='team2_matches',on_delete=models.CASCADE)
    ref = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    countDown = models.DateField(null=True)
    location = models.ForeignKey('CourtSchedule',on_delete=models.CASCADE,null=True)
    team1Wins = models.IntegerField(default=0)
    team2Wins = models.IntegerField(default=0)

#https://stackoverflow.com/questions/28712848/composite-primary-key-in-django
class CourtSchedule(models.Model):
    class Meta:#composite primary key
        unique_together = (('location','id'),)
    location = models.CharField(max_length=128)
    id = models.ForeignKey(MatchTable,on_delete=models.CASCADE,primary_key=True)

    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    matchDetail = models.CharField(max_length=255,blank=True) 
