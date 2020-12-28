from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import json


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        token["username"] = user.username
        token["last_login"] = user.last_login.__str__()
        return token
