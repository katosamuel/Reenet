from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .services import *

# Create your views here.

class SignalView(APIView):
    def get(self, request, signal_id=None):
        if signal_id is not None:
            return get_single_signal(signal_id)
        return get_signals()
    
    def post(self, request):
        return post_signal(request)
    
    def delete(self, request, signal_id):
        return delete_signal(signal_id, request)
        