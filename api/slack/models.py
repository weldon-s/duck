from django.db import models
from team.models import Dancer, Season

# Create your models here.
class Workspace(models.Model):
    token = models.CharField(max_length=100)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)

class User(models.Model):
    '''
    This allows us to match dancers to Slack users, so we can send them appropriate messages
    '''
    dancer = models.ForeignKey(Dancer, on_delete=models.CASCADE)
    slack_id = models.CharField(max_length=100)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)