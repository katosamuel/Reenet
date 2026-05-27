from rest_framework import serializers
from .models import (Signals)

class SignalSerializer(serializers.ModelSerializer):
    # author = serializers.ReadOnlyField()
    # post_image = serializers.ImageField()
    class Meta:
        model = Signals
        fields = ["id", "signal_text", "created_at"]