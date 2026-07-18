from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.comments.serializers import (CommentSerializer, CreateCommentSerializer)
from apps.comments.queries import CommentQueries
from apps.comments.services import (CreateComment)                                                                                                                                                                                                                                                                                           

# Create your views here.

class CommentView(APIView):
    def get(self, request, post_id):
        # comments = get_comments(request, post_id)
        # serializer = CommentSerializer(comments, many=True)
        # return Response(serializer.data, status=200)
        pass
    
    # def post(self, request,  post_id):
    #     user = request.user 
    #     serializer = CommentSerializer(data=request.data)
    #     if serializer.is_valid():
    #         post_comment(user=user, post_id=post_id, validated_data=serializer.validated_data)
    #         return Response(serializer.data, status=200)
    #     return Response(serializers.errors, status=400)
        
    
    # def delete(self, request):
    #     return Response()
    
class CommentListView(APIView):
    def get(self, request, **kwargs) -> Response:
        post_id = kwargs.get("post_id")
        comments = CommentQueries.get_comment_list(post_id=post_id)
        serializers = CommentSerializer(comments, many=True)
        print(serializers.data)
        return Response(serializers.data, status=200)
    
    def post(self, request, **kwargs) -> Response:
        post_id = kwargs.get("post_id")
        user = request.user
        create_serializer = CreateCommentSerializer(data=request.data)
        create_serializer.is_valid(raise_exception=True)
        comment = CreateComment.execute(user=user, post_id=post_id, content=create_serializer.validated_data["content"])
        serializer = CommentSerializer(comment)
        print(serializer.data)
        return Response(serializer.data, status=201)

