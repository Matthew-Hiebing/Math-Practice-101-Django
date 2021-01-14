from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import AccessToken
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


class UserCreate(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                user.create_blank_user_parameters()
                # Create refresh and access tokens for user.
                tokenr = TokenObtainPairSerializer().get_token(user)
                tokena = AccessToken().for_user(user)

                json = serializer.data
                json.pop("password")
                json['access'] = tokena.__str__()
                json['refresh'] = tokenr.__str__()

                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
