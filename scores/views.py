from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='/accounts/login/')
def scores(request):
    '''
    Returns the correct_answer_count, incorrect_answer_count, and
    total_questions_answered from the tally_results function.
    '''
    return render(request, 'scores/scores.html', {
        'correct_answer_count': tally_results(request)
        ['correct_answer_count'],
        'incorrect_answer_count': tally_results(request)
        ['incorrect_answer_count'],
        'total_questions_answered': tally_results(request)
        ['total_questions_answered']
    })


@login_required(login_url='/accounts/login/')
def tally_results(request):
    '''
    Identifies the current user, counts the number of 'Correct' and 'Incorrect'
    answers, and sums the total questions answered for the current user. Once
    this information is tally'd, the results are updated in the Scores class.
    '''
    correct_answer_count = request.user.record_set.all().filter(
        question_status='Correct').count()
    incorrect_answer_count = request.user.record_set.all().filter(
        question_status='Incorrect').count()
    total_questions_answered = correct_answer_count + incorrect_answer_count

    score = request.user.score_set.get()
    score.number_of_correct_answers = correct_answer_count
    score.number_of_incorrect_answers = incorrect_answer_count
    score.total_questions_answered = total_questions_answered

    score.save(update_fields=['number_of_correct_answers',
                              'number_of_incorrect_answers',
                              'total_questions_answered'])

    return {'correct_answer_count': correct_answer_count,
            'incorrect_answer_count': incorrect_answer_count,
            'total_questions_answered': total_questions_answered}


@login_required(login_url='/accounts/login/')
def request_score_details(request):
    '''
    Identified the current user and returns the current
    number_of_correct_answers, the number_of_incorrect_answers and the
    total_questions_answered from the Scores class.
    '''
    score = request.user.score_set.get()
    return render(request, 'scores/scores.html', {
        'correct_answer_count': score.number_of_correct_answers,
        'incorrect_answer_count': score.number_of_incorrect_answers,
        'total_questions_answered': score.total_questions_answered
    })
