from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Score(models.Model):
    """
    ===
        Scoring System
    ===
    This class creates a row for each new user that contains their user_id,
    number of correctly answered problems, number of incorrectly answered
    problems, and the total number of problems they attempted.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_incorrect_answers = models.IntegerField(default=0,null=False)
    number_of_correct_answers = models.IntegerField(default=0,null=False)
    total_questions_answered = models.IntegerField(default=0,null=False)


class Record(models.Model):
    """
    ===
        User Gaming Records
    ===
    This class records the characteristics of the game while the user is
    playing.  It records the date/time for each problem, the problem they were
    given, their answer, and the true answer.  The user will only be given math
    problems that require a whole number answer.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    math_problem = models.CharField(null=False,max_length=10)
    date_time = models.DateTimeField(null=False)
    user_answer = models.IntegerField(null=False)
    true_answer = models.IntegerField(null=False)


class SplashScreenPreference(models.Model):
    """
    ===
    User Preference for Splash Screens
    ===
    This stores the user's preference's for splash screen visibility.  After
    the user logs in and navigates to the math page they will be presented a
    splash screen that will introduce them to the game and provide them a
    general workflow and rules outline.  The spashscreen will continue to
    display after each refresh unless the user checks a box saying,"don't show
    me this anymore".

    The 'display_on_refresh' will stay 'True' until the user ops out of the
    splash screen.  Once they opt out the boolean will flip to 'False' and they
    won't see the splash screen anymore.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    splash_screen = models.CharField(null=True, max_length=100) # Not sure if this is needed
    display_on_refresh = models.BooleanField(default=True)


class SplashScreen(models.Model):
    """
    ===
    Splash Screen Class
    ===
    Defines a splash screen's characteristics.
    """
    splash_screen_name = models.CharField(max_length=100)
    splash_screen_message = models.CharField(max_length=500)
