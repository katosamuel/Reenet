from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CommentSerializer
from .services import *

# Create your views here.

class CommentView(APIView):
    def get(self, request, post_id):
        comments = get_comments(request, post_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request,  post_id):
        user = request.user 
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            post_comment(user=user, post_id=post_id, validated_data=serializer.validated_data)
            return Response(serializer.data, status=200)
        return Response(serializers.errors, status=400)
        
    
    def delete(self, request):
        return Response()