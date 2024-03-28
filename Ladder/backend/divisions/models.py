from django.db import models
from django.core.exceptions import ValidationError
from users.models import User
from team.models import Team
from django.db.models import Max

class Division(models.Model):
    name = models.CharField(max_length=55,primary_key=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    publicProfile = models.ImageField(upload_to='profile_images', blank= True, null=True)
    class Status(models.TextChoices):
       INPROGRESS = 'i', 'inProgress'
       NotStarted = 'n', 'notStated'
       VOID = 'v', 'void'
       FINISHED = 'f', 'finished'
    status = models.CharField(max_length=1,choices=Status.choices,null=True)
    
    def __str__(self):
        return self.name
    
class TeamInDivision(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    position = models.PositiveIntegerField()
    class Meta:
        unique_together = ('division', 'team')

    def __str__(self):
        return f"{self.team} in {self.division}"
    
    # def clean(self):
    #     # Check if there's any other team in the same division with the same position
    #     if TeamInDivision.objects.filter(division=self.division, position=self.position).exclude(pk=self.pk).exists():
    #         raise ValidationError("A team in this division already occupies this position.")
        
    # def save(self, *args, **kwargs):
    #     if not self.position:
    #         # Calculate the next possible position for the team in the division
    #         max_position = TeamInDivision.objects.filter(division=self.division).aggregate(Max('position'))['position__max']
    #         if max_position is None:
    #             max_position = 0
    #         self.position = max_position + 1

    #     super().save(*args, **kwargs)
        