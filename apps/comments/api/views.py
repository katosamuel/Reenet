from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.comments.serializers import (CommentSerializer, CreateCommentSerializer)
from apps.comments.queries import CommentQueries
from apps.comments.services import (CreateComment, DeleteComment)                                                                                                                                                                                                                                                                                           

# Create your views here.

class CommentView(APIView):

    @staticmethod
    def ids(data) -> tuple:
        post_id = data.get("post_id")
        comment_id = data.get("comment_id")
        return post_id, comment_id
    
    def get(self, request, **kwargs) -> Response:
        post_id, comment_id = self.ids(kwargs)
        comment = CommentQueries.get_comment(post_id=post_id, comment_id=comment_id)
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=200)
        
    
    def patch(self, request, **kwargs) -> Response:
        post_id, comment_id = self.ids(kwargs)
        serializer = CommentSerializer(data=request.data)
        return Response(serializer.errors, status=400)
        
    
    def delete(self, request, **kwargs) -> Response:
        post_id, comment_id = self.ids(kwargs)
        delete_comment = DeleteComment.execute(post_id=post_id, comment_id=comment_id)
        if delete_comment == True:
            return Response({"message": "comment deleted"}, status=200)
        return Response({"error": "comment deletion error"}, status=400)
    
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

