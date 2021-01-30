from rest_framework.views import APIView
from rest_framework import status
from game.models import SplashScreen, SplashScreenPreference, Record
from rest_framework.response import Response
from .serializers import GamePropertiesSerializer
import json
import datetime
import pytz


class GamePropertiesView(APIView):
    def get(self, request, format='json'):
        # Grab the user that is logged in
        logged_in_user = request.user

        # Grab the user's splash screen preferences
        user_splash_screen_preference = logged_in_user.splashscreenpreference_set.all().get(splash_screen='Math')

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


class SetSplashScreenPreference(APIView):
    """
    This function sets the splash screen preference of the user
    based on whether they clicked the checkbox or not.
    """
    def post(self, request, format='json'):
        SplashScreenPreference.set_splash_screen_preference(
            user=request.user,
            params=json.loads(request.body)
        )

        return Response(data={"status": "success"},
                        status=status.HTTP_202_ACCEPTED)


class SubmitScoreDetails(APIView):
    """
    Submits math problem details including the math problem, the date and time
    when the POST was made, the user's answer, the true answer, and the results
    of the user as 'correct' or 'incorrect'.
    """
    @staticmethod
    def tally_results(request):
        '''
        Identifies the current user, counts the number of 'Correct' and
        'Incorrect' answers, and sums the total questions answered for the
        current user. Once this information is tally'd, the results are updated
        in the Scores class.
        '''
        correct_answer_count = request.user.record_set.all().filter(
            question_status='correct').count()
        incorrect_answer_count = request.user.record_set.all().filter(
            question_status='incorrect').count()
        total_questions_answered = (
            correct_answer_count + incorrect_answer_count
        )

        score = request.user.score
        score.number_of_correct_answers = correct_answer_count
        score.number_of_incorrect_answers = incorrect_answer_count
        score.total_questions_answered = total_questions_answered

        score.save(update_fields=[
            'number_of_correct_answers',
            'number_of_incorrect_answers',
            'total_questions_answered'
        ])

        return {
            'correct_answer_count': correct_answer_count,
            'incorrect_answer_count': incorrect_answer_count,
            'total_questions_answered': total_questions_answered
        }

    def post(self, request, format='json'):
        timezone = pytz.timezone("US/Central")
        date = timezone.localize(datetime.datetime.now())
        params = json.loads(request.body)
        record = Record(
            user=request.user,
            math_problem=params['math_problem'],
            date_time=date,
            user_answer=params['user_answer'],
            true_answer=params['true_answer'],
            question_status=params['question_status']
        )
        record.save()

        self.tally_results(request)

        return Response(data={
            "status": "success"},
            status=status.HTTP_202_ACCEPTED
        )


class RequestScoreDetails(APIView):
    def get(self, request, format='json'):
        """
        Identified the current user and returns the current
        number_of_correct_answers, the number_of_incorrect_answers and the
        total_questions_answered from the Scores class.
        """

        score = request.user.score

        return Response(data={
            'correct_answer_count': score.number_of_correct_answers,
            'incorrect_answer_count': score.number_of_incorrect_answers,
            'total_questions_answered': score.total_questions_answered},
            status=status.HTTP_200_OK
        )
