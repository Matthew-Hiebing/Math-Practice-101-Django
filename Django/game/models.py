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
  number_of_correct_answers = models.IntegerField(null=True)
  number_of_incorrect_answers = models.IntegerField(null=True)
  total_questions_answered = models.IntegerField(null=False)
