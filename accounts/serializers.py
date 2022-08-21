from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from game.models import GameUser
import datetime


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        # Set the date and time after login.
        user.last_login = datetime.datetime.now()
        user.save()
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token["username"] = user.username
        token["last_login"] = user.last_login.__str__()
        token["is_staff"] = user.is_staff
        return token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameUser
        fields = "__all__"

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            # Create a blank preference
        instance.save()
        return instance
