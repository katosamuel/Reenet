from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .services import *
from .serializers import *

# Create your views here.
def get_token(user):
    token = RefreshToken.for_user(user)
    return token

def user_data(token, user):
    data = {
            "id": user.id,
            "email": user.email,
            "access": str(token.access_token),
            "refresh_token": str(token)
            }
    return data

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = register_user(serializer.validated_data)
        token = get_token(user)
        data = user_data(token=token, user=user)
        return Response(data, status=201)
        # return Response(serializer.errors)
           
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = login_user(serializer.data)
        token = get_token(user)
        data = user_data(user=user, token=token)
        return Response(data, status=200)

class Profile(APIView):
    def get(self, request):
        pass
        # return Response()

    def post(self):
        pass