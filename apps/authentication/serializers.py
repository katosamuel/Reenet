from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()

class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8)
    class Meta:
        model = User
        fields = ["id", "email", "password"]

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value
        
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8)

class ProfileSerializer(serializers.ModelSerializer):
    #profile = serializers.ImageField()
    email = serializers.EmailField(source="user.email", read_only=True)
    class Meta:
        model = Profile
        fields = ["id", "username", "email", "bio", "avatar", "time_stamp"]
        read_only = ["id", "email", "time_stamp"]

