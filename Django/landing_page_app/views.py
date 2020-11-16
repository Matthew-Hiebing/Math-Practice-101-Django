from django.shortcuts import render
from landing_page_app.forms import new_user
import random

# Create your views here.

def landing_page(request):
    return render(request, 'landing_page.html')

def game(request):
    num1 = random.randint(0, 12)
    num2 = random.randint(0, 12)
    problemResult = num1 * num2
    return render(request, 'game.html', {"problemResult" : problemResult})

def users(request):
    form = new_user()
    if request.method == 'POST':
        form = new_user(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return landing_page(request)
        else:
            print("Error, form invalid")
    return render(request,'new_user.html',{'form':form})
