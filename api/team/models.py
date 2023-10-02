from django.db import models

class Style(models.Model):
    name = models.CharField(max_length=100)
class Team(models.Model):
    name = models.CharField(max_length=100)

class Season(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

class Dancer(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    date_of_birth = models.DateField()

    # These two can change from season to season so we can't just use a Boolean field
    choreographer_seasons = models.ManyToManyField(Season, related_name="choreographer_set")
    captain_seasons = models.ManyToManyField(Season, related_name="captain_set")

# This is for modelling teams within a team (e.g. ballet team, jazz team)
class Subteam(models.Model):
    name = models.CharField(max_length=100)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    dancers = models.ManyToManyField(Dancer)

class Routine(models.Model):
    # The name of the routine is what it will be called onstage
    # We will also eventually have a label for the dance (e.g. Large Jazz) based on the style and number of dancers
    name = models.CharField(max_length=100)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    choreographers = models.ManyToManyField(Dancer, related_name="choreographer_set")
    dancers = models.ManyToManyField(Dancer, related_name="dancer_set")

    # This is the subteam that the routine is for and will dictate which dancers can be added to the routine
    subteam = models.ForeignKey(Subteam, on_delete=models.CASCADE)

# This allows dancers to accept or reject offers for routines
# When a dancer accepts an offer, they are added to the corresponding routine
class Offer(models.Model):
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)
    dancer = models.ForeignKey(Dancer, on_delete=models.CASCADE)
    # Accepted is null if the offer has not been accepted or rejected yet
    accepted = models.BooleanField(null=True)