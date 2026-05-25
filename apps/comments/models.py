from django.db import models
from apps.authentication.models import User
from apps.posts.models import Signals

# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(User, related_name="my_comments", on_delete=models.CASCADE)
    post = models.ForeignKey(Signals, related_name="comments", on_delete=models.CASCADE)
    text_content = models.CharField(max_length=500)
    image_content = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    time_stamp = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-time_stamp"]

    def __str__(self):
        return f"{self.user} replying to {self.post}: {self.text_content}"