from django.db import models

# Create your models here.

class Match(models.Model):
	sport_choices = (
			('Cricket', 'Cricket'),
			('Football', 'Football'),
			)
	team_choices = (
			('Umiam', 'Umiam'),
			('Barak', 'Barak'),
			)

	match_time = models.DateTimeField(auto_now=False)
	sport = models.CharField(choices=sport_choices)
	team1 = models.CharField(choices=team_choices)
	team2 = models.CharField(choices=team_choices)

	location = models.CharField(max_length=20)

class Comment(models.Model):

	match = models.ForeignKey(Match)

	timestamp = models.DateTimeField(auto_now=True)
	comment_text = models.TextField(max_length=1000)