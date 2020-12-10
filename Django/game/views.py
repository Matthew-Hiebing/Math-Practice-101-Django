from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from game.models import SplashScreen, SplashScreenPreference, Record
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import datetime


def get_splash_screen(request, name):
    """
    Function identifies current user, grab's the user's preference to see
    the splash screen or not, filters down to the splash screen name, and
    check's the user's preference to 'display_on_refresh' or not.  If the user
    doesn't want to see the splash screen 'False' is passed to 'presence'.
    """
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


@csrf_exempt
def set_splash_screen_preference(request):
    """
    This function sets the splash screen preference of the user
    based on whether they clicked the checkbox or not.
    """
    if request.method == 'POST':
        params = json.loads(request.body)
        # Now we execute the class method to set the preference
        SplashScreenPreference.set_splash_screen_preference(
            user=request.user,
            params=params
            )
        return JsonResponse({"status": "The user setting was completed!"})
    else:
        return JsonResponse({"status": "That was not a valid request"})


@login_required(login_url='/accounts/login/')
def game(request):
    '''
    Grabs the splash screen message and renders the HTML showing the splash
    screen and its contents.
    '''
    # Grab the splash screen
    splash_screen_dictionary = get_splash_screen(request, name='Math')
    return render(request, 'game/game.html', {
        "splash_screen": splash_screen_dictionary
    })


@login_required(login_url='/accounts/login/')
# @csrf_exempt
def submit_score_details(request):
    '''
    Submits math problem details including: the math problem, the date and time
    when the POST was made, the user's answer, the true answer, and the results
    of the user as 'correct' or 'incorrect'.
    '''

    if request.method == 'POST':
        params = json.loads(request.body)
        record = Record(user=request.user,
                        math_problem=params['math_problem'],
                        date_time=datetime.datetime.now(),
                        user_answer=params['user_answer'],
                        true_answer=params['true_answer'],
                        question_status=params['question_status'])
        record.save()
        return JsonResponse({"status": "The score details were sent!"})
    else:
        return JsonResponse({"status": "That was not a valid request"})

    # Score(user=request.user,
    #       number_of_correct_answers=attempt_params
    #       ['number_of_correct_answers'],
    #       number_of_incorrect_answers=attempt_params
    #       ['number_of_incorrect_answers'],
    #       total_questions_answered=attempt_params
    #       ['total_questions_answered'],
    #       )
