from rest_framework import serializers
from .models import (Signals)

class SignalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signals
        fields = ["id", "signal_text", "created_at"]