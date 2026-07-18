from rest_framework import serializers
from apps.comments.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "user", "post", "content", "created_at"]
        # read_only = ["id", "user", "post"]

class CreateCommentSerializer(serializers.ModelSerializer):
    content = serializers.CharField(max_length=300)
    class Meta:
        model = Comment