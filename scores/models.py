from django.db import models


# Create your models here.

class Match(models.Model):
    sport_choices = (
        ('Aquatics', 'Aquatics'),
        ('Athletics', 'Athletics'),
        ('Badminton', 'Badminton'),
        ('Basketball', 'Basketball'),
        ('Cricket', 'Cricket'),
        ('Football', 'Football'),
        ('Hockey', 'Hockey'),
        ('Squash', 'Squash'),
        ('Tennis', 'Tennis'),
        ('Table Tennis', 'Table Tennis'),
        ('Volleyball', 'Volleyball'),
        ('Weightlifting', 'Weightlifting')
    )
    team_choices = (
        ('Umiam', 'Umiam'),
        ('Barak', 'Barak'),
        ('Kameng', 'Kameng'),
        ('Dihing', 'Dihing'),
        ('Manas', 'Manas'),
        ('Lohit', 'Lohit'),
        ('Siang', 'Siang'),
        ('Bramhaputra', 'Bramhaputra'),
        ('Kapili', 'Kapili'),
        ('Dhansiri', 'Dhansiri'),
        ('Subansiri', 'Subansiri'),
        ('MSH', 'MSH')
    )

    match_time = models.DateTimeField(auto_now=False)
    match_name = models.CharField(max_length=50)
    match_description = models.CharField(max_length=50)
    sport = models.CharField(choices=sport_choices, max_length=30)
    team1 = models.CharField(choices=team_choices, max_length=30)
    team2 = models.CharField(choices=team_choices, max_length=30)
    location = models.CharField(max_length=100)
    match_id = models.SlugField(max_length=8)
    def __str__(self):
        return self.match_name+" ("+self.match_description+") "+self.team1+" vs "+self.team2

class Comment(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    comment_text = models.TextField(max_length=1000)
    def __str__(self):
        return self.match.match_name+" "+self.comment_text
