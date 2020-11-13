from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import datetime

# Create your views here.

# def index(request):
#     my_dict = {'welcome_message': "Hello brave student, welcome to Math 101. In this game you will be"
#                " presented a random math problem that you will need to solve.  It will be a"
#                " random choice of subtraction, addition, division, and multiplication. You"
#                " will have 2 guesses per problem, after that, GAMEOVER!"}  # Template we want to use shown as the dictionary key.

#     return render(request,'landingPageHTML/main.html',context=my_dict) #"landingPage" is referring to the landingPage folder in the static folder.


def return_html(request):
    return render(request, 'landingPageHTML/test.html')
