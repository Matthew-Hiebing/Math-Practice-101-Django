from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from game.models import Score, Record
from django.http import JsonResponse
import json
# Create your views here.


@login_required(login_url='/accounts/login/')
def scores(request):
    returned_tally_results = tally_results(request)
    return render(request, 'scores/scores.html', {
        'correct_answer_count': returned_tally_results
        ['correct_answer_count'],
        'incorrect_answer_count': returned_tally_results
        ['incorrect_answer_count'],
        'total_questions_answered': returned_tally_results
        ['total_questions_answered']
    })


def tally_results(request):
    '''
    Identifies the current user, counts the number of 'Correct' and 'Incorrect'
    answers, and sums the total questions answered for the current user. Once
    this information is tally'd, the results are sent to the Scores class where
    the Scores for the current user are updated.
    '''
    current_user = request.user

    correct_answer_count = current_user.record_set.all().filter(
        question_status='Correct').count()

    incorrect_answer_count = current_user.record_set.all().filter(
        question_status='Incorrect').count()

    total_questions_answered = correct_answer_count + incorrect_answer_count

    # Here we find the score for the user and update the values then save score
    score = current_user.score_set.get(user=current_user)
    score.number_of_correct_answers = correct_answer_count
    score.number_of_incorrect_answers = incorrect_answer_count
    score.total_questions_answered = total_questions_answered
    score.save(update_fields=['number_of_correct_answers',
                              'number_of_incorrect_answers',
                              'total_questions_answered'])

    return {'correct_answer_count': correct_answer_count,
            'incorrect_answer_count': incorrect_answer_count,
            'total_questions_answered': total_questions_answered}


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
