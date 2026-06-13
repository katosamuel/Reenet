from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Signals(models.Model):
    # author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    # post_image = models.ImageField(upload_to="post_images/", max_length=255)
    signal_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return self.signal_text