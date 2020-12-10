from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from game.models import Score
from django.http import JsonResponse
import json
# Create your views here.


@login_required(login_url='/accounts/login/')
def scores(request):
    return render(request, 'scores/scores.html')


def request_score_details(request):
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
        return JsonResponse({"status": "That was not a valid request"})
