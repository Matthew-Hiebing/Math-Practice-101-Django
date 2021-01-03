from rest_framework.views import APIView
from rest_framework import permissions, status, authentication
from game.models import SplashScreen
from rest_framework.response import Response
from .serializers import GamePropertiesSerializer


class GamePropertiesView(APIView):
    def get(self, request, format='json'):
        # Grab the user that is logged in
        logged_in_user = request.user

        # Grab the user's splash screen preferences
        user_splash_screen_preference = logged_in_user.\
            splashscreenpreference_set.all().get(splash_screen='Math')

        # Grab contents of splashscreen from 'Math'
        splash_screen = SplashScreen.objects.get(splash_screen_name='Math')

        # Dictionary containing preference and splash screen message
        game_properties = {
            'splash_screen': {
                'preference': user_splash_screen_preference,
                'content': splash_screen
            }
        }

        serializer = GamePropertiesSerializer(game_properties)

        return Response(data=serializer.data)
