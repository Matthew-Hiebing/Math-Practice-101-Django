from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from game.models import Score, Record
from django.http import JsonResponse
import json
# Create your views here.


@login_required(login_url='/accounts/login/')
def scores(request):
    return render(request, 'scores/scores.html')


def tally_results(request):
    '''
    Counts the number 'Correct' answers, 'Incorrect' answers, and sums the 'total questions answered' for the current user. Once this information is tally'd, the results are sent to the Scores class and the Scores for the current user are updated.
    '''
    # count how many 'correct' answers there are
    # count how many 'incorrect' answers there are
    # sum counts of 'correct' and 'incorrect' answers to get
    # total_questions_answered

    correct_answer_count = Record.objects.all().filter(
        question_status='Correct').count()

    incorrect_answer_count = Record.objects.all().filter(
        question_status='Incorrect').count()

    total_questions_answered = correct_answer_count + incorrect_answer_count


def request_score_details(request):
    '''
    Sends a GET request for the current number_of_correct_answers, the
    number_of_incorrect_answers, and the total_questions_answered from the
    Scores class.
    '''
    if request.method == 'GET':
        params = json.loads(request.body)
        score = Score(user=request.user,
                      number_of_correct_answers=params
                      ['number_of_correct_answers'],
                      number_of_incorrect_answers=params
                      ['number_of_incorrect_answers'],
                      total_questions_answered=params
                      ['total_questions_answered'],
                      )
        return JsonResponse({"status": "The score details were retrieved!"})
    else:
        return JsonResponse({"status": "That was not a valid request."})
