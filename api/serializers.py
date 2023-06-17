# photosapp/serializers.py
from rest_framework import serializers
# from .models import photos
from django.contrib.auth.models import User


from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    image_url = serializers.ReadOnlyField()

    class Meta:
        model = Image
        fields = ["image_url", "image", "timestamp","id"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop("image")

        return representation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        # Perform custom validation on the data
        # For example, check if the username/password combination is valid
        # If validation fails, raise serializers.ValidationError
        # If validation passes, return the validated data
        return data