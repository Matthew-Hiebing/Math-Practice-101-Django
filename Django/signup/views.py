from django.shortcuts import render
from signup.forms import new_user
from homepage.views import homepage


# Create your views here.
def users(request):
    form = new_user()
    if request.method == 'POST':
        form = new_user(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return homepage(request)
        else:
            print("Error, form invalid")
    return render(request, 'signup.html', {'form': form})
