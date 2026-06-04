from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
# from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from .models import *
from django.contrib.auth import get_user_model

User = get_user_model()

def register_user(validated_data):
    user = User.objects.create_user(email=validated_data["email"], 
                                    password=validated_data["password"])
    return user


def login_user(validated_data):
    user = authenticate(email=validated_data["email"],
                        password=validated_data["password"])
    return user

def get_profile(profile_id=None):
    if not profile_id:
        return {"error": "id required"}
    
    profile = Profile.objects.get(id=profile_id)
    try:
        return profile
    except profile.DoesNotExist:
        return {"message": "profile not found"}
    
# def post_profile(validated_data):
#     profile = Profile.objects.create(

#     )
#     return profile
