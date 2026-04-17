from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models


from octofit_tracker.models import Team, Activity, Leaderboard, Workout

from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Clear all collections
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users
        users = [
            User.objects.create_user(username='superman', email='superman@dc.com', password='superpass', team=dc),
            User.objects.create_user(username='batman', email='batman@dc.com', password='batpass', team=dc),
            User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', password='wonderpass', team=dc),
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='ironpass', team=marvel),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='spiderpass', team=marvel),
            User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='cappass', team=marvel),
        ]

        # Create Activities
        activities = [
            Activity.objects.create(user=users[0], type='flight', duration=60),
            Activity.objects.create(user=users[1], type='martial arts', duration=45),
            Activity.objects.create(user=users[2], type='strength', duration=50),
            Activity.objects.create(user=users[3], type='tech', duration=40),
            Activity.objects.create(user=users[4], type='agility', duration=30),
            Activity.objects.create(user=users[5], type='leadership', duration=55),
        ]

        # Create Workouts
        workouts = [
            Workout.objects.create(name='Super Strength', description='Strength workout for heroes'),
            Workout.objects.create(name='Flight Training', description='Flight workout for heroes'),
        ]

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=300)
        Leaderboard.objects.create(team=dc, points=250)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))

# Models for reference (should be in octofit_tracker/models.py):
# class Team(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#
# class Activity(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     type = models.CharField(max_length=100)
#     duration = models.IntegerField()
#
# class Workout(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#
# class Leaderboard(models.Model):
#     team = models.ForeignKey(Team, on_delete=models.CASCADE)
#     points = models.IntegerField()
