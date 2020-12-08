from django.shortcuts import render

# Create your views here.


def scores(request):
    return render(request, 'scores/scores.html')
