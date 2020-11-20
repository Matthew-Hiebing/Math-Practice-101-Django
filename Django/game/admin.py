from django.contrib import admin

# Register your models here.
from game import models

admin.site.register(models.Score)
admin.site.register(models.Record)
admin.site.register(models.SplashScreen)
admin.site.register(models.SplashScreenPreference)
