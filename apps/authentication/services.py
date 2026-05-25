from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
# from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from .models import *

def register_user(validated_data):
    user = User.objects.create_user(username=validated_data["username"],
                                    email=validated_data["email"], 
                                    password=validated_data["password"])
    return user


def login_user(validated_data):
    user = authenticate(username=validated_data["username"], 
                        email=validated_data["email"],
                        password=validated_data["password"])
    return user