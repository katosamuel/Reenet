from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from .models import *

def register(email, password):
    if User.objects.filter(email=email).exists():
        raise AuthenticationFailed("user with this email already exists")
    user = User.objects.create(email=email, password=password)
    return user

def login(email, password):
    user = None
    return user