from django.shortcuts import get_object_or_404
from apps.posts.models import Post

class PostQueries:
    @staticmethod 
    def list_posts():
        posts = Post.objects.all()
        return posts

    @staticmethod
    def get_post(post_id):
        if  not post_id:
            return False
        try:
            post = Post.objects.get(id=post_id)
            return post
        except Post.DoesNotExist:
            return None