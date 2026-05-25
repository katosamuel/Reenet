from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .services import *
from .serializers import *

# Create your views here.
def get_token(user):
    token = RefreshToken.for_user(user)
    return ({"access": str(token.access_token),
            "refresh_token": str(token)})

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = register_user(serializer.validated_data)
        return Response(get_token(user), status=201)
        # return Response(serializer.errors)
           
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = login_user(serializer.data)
        return Response({"message": "logged in successfully"}, get_token(user))