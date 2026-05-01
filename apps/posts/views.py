from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .services import *

# Create your views here.

class SignalView(APIView):
    def get(self, request):
        return get_signals()
    
    def post(self, request):
        return post_signal(request)
    
    def delete(self, signal_id, request):
        return delete_signal(signal_id, request)