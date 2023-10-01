# photosapp/serializers.py
from rest_framework import serializers
# from .models import photos
from django.contrib.auth.models import User


from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    image_url = serializers.ReadOnlyField()

    class Meta:
        model = Image
        fields = ["title","image_url", "media", "timestamp","id","user_id"]
        
    def create(self, validated_data):
        # Get the currently logged-in user from the context
        user = self.context['request'].user
        image = Image.objects.create(user=user, **validated_data)
        return image

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop("media")

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
    
class EditImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["title"] 
        
class DeleteImageSerializer(serializers.Serializer):
    pass