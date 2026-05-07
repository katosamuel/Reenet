from rest_framework.response import Response
from rest_framework.views import APIView
from .services import *
from .serializers import *

# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
        #return Response()
    
class LoginView(APIView):
    def post(self, request):

        return Response()