from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from homepage import views
from game.models import Score, SplashScreenPreference
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions, status
from .serializers import MyTokenObtainPairSerializer, UserSerializer

# Super User Information:
# User Matthew.Hiebing
# Email: Matthew.Hiebing@gmail.com
# Password: testpass1029

# User Mary.Hiebing
# Password: 7ee5eap3npZeNZY


class ObtainTokenPairWithExtraInfo(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create a blank_score row for each user when they make an account
            new_game_score = Score(user=user,
                                   number_of_correct_answers=0,
                                   number_of_incorrect_answers=0,
                                   total_questions_answered=0
                                   )
            new_game_score.save()
            # Create a SplashScreenPreference for the user on signup.
            SplashScreenPreference(user=user,
                                   splash_screen="Math",
                                   display_on_refresh=True
                                   ).save()
            login(request, user)
            # Log the user in
            return redirect(views.homepage)
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Log the user in
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return render(request, 'accounts/login_successful.html')
    else:
        form = AuthenticationForm(request.POST)
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return render(request, 'accounts/logout.html')


class UserCreate(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                json.pop("password")
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

