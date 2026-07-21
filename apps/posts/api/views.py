from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.posts.queries.post_queries import PostQueries
from apps.posts.services import (CreatePost, UpdatePost, DeletePost)
from apps.posts.serializers.post import (CreatePostSerializer, PostSerializer)
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from apps.posts.permissions import IsPostOwner

# Create your views here.

class SignalListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request) -> Response:
        posts = PostQueries().list_posts()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=200)

class SignalCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request) -> Response:
        serializer = CreatePostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post = CreatePost().execute(author=request.user, content=serializer.validated_data["signal_text"])
        post_serializer = PostSerializer(post)
        return Response(post_serializer.data, status=201) 

class SignalDetailView(APIView):
    permission_classes = [IsAuthenticated, IsPostOwner]
    def get(self, request, **kwargs) -> Response:
        post_id = kwargs.get("post_id")
        post = PostQueries().get_post(post_id=post_id)
        serializer = PostSerializer(post)
        if post is not None:
            return Response(serializer.data, status=200)
        return Response({"error": "post not found"})

    def patch(self, request, **kwargs) -> Response:
        post_id = kwargs.get("post_id")
        post = PostQueries.get_post(post_id=post_id)
        serializer = CreatePostSerializer(post, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        post = UpdatePost().execute(post=post, validated_data=serializer.validated_data)
        post_serializer = PostSerializer(post)
        return Response(post_serializer.data, status=200)
    
    def delete(self, request, **kwargs) -> Response:
        post_id = kwargs.get("post_id")
        post = PostQueries.get_post(post_id=post_id)
        self.check_object_permissions(request, post)
        delete_post = DeletePost().execute(post_id=post_id)
        
        if delete_post == True:
            return Response({"message": "post deleted successfully"}, status=200)
        return Response({"message": "post not found"}, status=404)
        
        