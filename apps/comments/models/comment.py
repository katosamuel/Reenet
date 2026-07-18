from django.db import  models
from apps.posts.models import Post
from django.contrib.auth import get_user_model

User = get_user_model()

class Comment(models.Model):
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, related_name="post", on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=300, null=True)
    created_at = models.DateField(auto_now=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content