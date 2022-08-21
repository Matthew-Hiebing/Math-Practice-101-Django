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
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                primary_key=True,)
    number_of_correct_answers = models.IntegerField(default=0, null=False)
    number_of_incorrect_answers = models.IntegerField(default=0, null=False)
    total_questions_answered = models.IntegerField(default=0, null=False)

    def __str__(self):
        return str(self.user)


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
    math_problem = models.CharField(null=False, max_length=10)
    date_time = models.DateTimeField(null=False)
    user_answer = models.IntegerField(null=False)
    true_answer = models.IntegerField(null=False)
    question_status = models.CharField(null=False, max_length=10,
                                       default='unknown')

    def __str__(self):
        return f"{self.user}, {self.math_problem}, {self.question_status}"


class SplashScreenPreference(models.Model):
    """
    ===
    User Preference for Splash Screens
    ===
    This stores the user's preferences for splash screen visibility.  After
    the user logs in and navigates to the math page they will be presented a
    splash screen that will introduce them to the game and a
    general outline of the game.  The splash screen will continue to
    display after each refresh unless the user checks a box saying, "Don't
    show this message again.".

    The 'display_on_refresh' will remain 'True' until the user ops out of the
    splash screen.  Once they opt out, the boolean will flip to 'False' and
    they won't see the splash screen anymore.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    splash_screen = models.CharField(null=True, max_length=100)
    display_on_refresh = models.BooleanField(default=True)

    @staticmethod
    def set_splash_screen_preference(user, params):
        '''
        This static method function finds a splashscreen preference by splash
        screen name and sets the preference to whatever the user wanted.
        '''
        # Find the user object
        # Grab the user's preferences and filter by splash screen name
        splash_screen_preference_object = user.\
            splashscreenpreference_set.all().get(splash_screen=params[
                'splash_screen_name'])

        # Now we set the preference for display on refresh true or false
        splash_screen_preference_object.display_on_refresh = params[
            'display_on_refresh']

        splash_screen_preference_object.save()

        return splash_screen_preference_object

    def __str__(self):
        return f"{self.user} Display on refresh: {'Yes' if self.display_on_refresh else 'No'}"


class SplashScreen(models.Model):
    """
    ===
    Splash Screen Class
    ===
    Defines splash screen's characteristics.  Multiple splash screen
    names and messages can be created.
    """
    splash_screen_name = models.CharField(max_length=100)
    splash_screen_message = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.splash_screen_name}: {self.splash_screen_message}"


class GameUser(User):
    """
    ===
    Game User Class
    ===
    Creates initial user parameters for new users
    """
    class Meta:
        proxy = True

    def create_blank_user_parameters(self):
        # Create a splash screen preference, default "Yes"
        SplashScreenPreference(
            user=self,
            splash_screen="Math",
            display_on_refresh=True
            ).save()

        # Create initial score of 0 for new users
        Score(
            user=self,
            number_of_correct_answers=0,
            number_of_incorrect_answers=0,
            total_questions_answered=0
            ).save()
