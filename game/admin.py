from django.contrib import admin
from game import models
# Register your models here.
# The below models below will show up in Django's admin page.

admin.site.register(models.Score)
admin.site.register(models.Record)
admin.site.register(models.SplashScreen)
admin.site.register(models.SplashScreenPreference)

# admin.site.site_url = 'https://math-game-react-frontend.herokuapp.com/'
