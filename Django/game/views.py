from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from game.models import SplashScreen


def get_splash_screen(request, name):
    # Grab the user that is logeed in
    logged_in_user = request.user
    # Grab the splash screen preferences for the user
    user_splash_screen_preferences = logged_in_user.\
        splashscreenpreference_set.all()
    # Filter the splash screen preference by splash screen name
    user_preference = user_splash_screen_preferences.\
        filter(splash_screen=name)[0]
    # Now we check what the user wants
    if user_preference.display_on_refresh is True:
        # If True, the user prefers to see the splash screen
        # Grab the splash screen from the database
        splash_screen = SplashScreen.objects.all().filter(
            splash_screen_name=name)[0]
        # Return dictionary containing presence of the splash screen and the
        # splash screen message
        return({
            "presence": True,
            "message": splash_screen.splash_screen_message
        })
    else:
        return({
            "presence": False,
        })


@login_required(login_url='/accounts/login/')
def game(request):
    # Grab the splash screen
    splash_screen_dictionary = get_splash_screen(request, name='welcome')

    return render(request, 'game/game.html', {
        "splash_screen": splash_screen_dictionary
    })


def sudoku(request):
    get_splash_screen(request, name='sudoku')
