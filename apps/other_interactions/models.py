from django.db import models
from django.contrib.auth import get_user_model
from apps.posts.models import Post
# Create your models here.

User = get_user_model()

class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time_stamp']
        unique_together = ["follower", "following"]

class SavePost(models.Model):
    user = models.ForeignKey(User, related_name="saved_posts", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='saved_posts', on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time_stamp']
        unique_together = ["user", "post"]

class LikePost(models.Model):
    user = models.ForeignKey(User, related_name="liked_posts", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='liked_posts', on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time_stamp']
        unique_together = ["user", "post"]
