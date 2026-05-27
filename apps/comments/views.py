from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .services import *

# Create your views here.

class CommentView(APIView):
    def get(self, request, post_id):
        comments = get_comments(request, post_id)
        
        return Response(serializer.errors, status=400)
    
    def post(self):
        # serializer = None
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=200)
        # return Response()
        pass
    
    def delete(self, request):
        return Response()