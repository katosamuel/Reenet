from django.db import models

# Create your models here.

class Signals(models.Model):
    signal_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return self.signal_text