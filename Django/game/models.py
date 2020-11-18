from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Score(models.Model):
  """
    ===
    Emission Localization Heatmap
    ===
    In order to generate a 2D overview of the spatial distribution
    of where the methane leaks are likely to be located, we
    present a 2D heatmap. The heatmap is constructed from a large
    collection of points that have an associated "probability" to
    them.

    This data structure is a 2-Dimensional spatial distribution,
    it contains geolocation (latitudes, longitudes) information
    as well as the probability of a particular chemical species
    to be present at that geographic location.
    
    ===
    Fields
    ===

    - `location [GeoJSON Point](latitude, longitude)`
    - `probability [float]`
    
    ===
    Relationships
    ===

    - HeatmapProbabilityPoint belongs to Emission (Many to One)
    Individual probability point that together form localization
    probability heatmaps.
  """
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  number_of_correct_answers = models.IntegerField(null=True)
  number_of_incorrect_answers = models.IntegerField(null=True)
  total_questions_answered = models.IntegerField(null=False)