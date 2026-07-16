from rest_framework import serializers
from apps.posts.models import Post

class CreatePostSerializer(serializers.ModelSerializer):
    signal_text = serializers.CharField()

    class Meta:
        model = Post
        fields = ["signal_text"]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "author", "signal_text", "created_at"]

