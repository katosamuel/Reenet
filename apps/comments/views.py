from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CommentSerializer
from posts.models import Signals

# Create your views here.

class CommentView(APIView):
    def get(self, request, post_id):
        try:
            post = Signals.objects.get(id=post_id)
        except post.DoesNotExist:
            return Response({"error": "post not found"}, status=404)
        serializer = CommentSerializer(post, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    def post(self):
        return Response()
    
    def delete(self, request):
        return Response()