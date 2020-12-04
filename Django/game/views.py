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
    # Now we actually check what the user wants
    if user_preference.display_on_refresh is True:
        # This means that the user does want to see the splash screen
        # So we need to grab the splash screen from the database
        splash_screen = SplashScreen.objects.all().filter(
            splash_screen_name=name)[0]
        # Return a dictionary containing presence and the splash screen message
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
    # num1 = random.randint(0, 12)
    # num2 = random.randint(0, 12)
    # problemResult = num1 * num2

    # Grab the splash screen
    splash_screen_dictionary = get_splash_screen(request, name='welcome')

    return render(request, 'game/game.html', {
        "splash_screen": splash_screen_dictionary
    })


def sudoku(request):
    get_splash_screen(request, name='sudoku')
