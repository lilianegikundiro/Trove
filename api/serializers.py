# photosapp/serializers.py
from django.forms import ValidationError
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
# from .models import photos
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator
from api.validators2 import username_validator,max_length_validator,min_length_validator,password_validator
from rest_framework.validators import UniqueValidator

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
 
    username = serializers.CharField(
        max_length=30,  # Set the maximum length to 30 characters
        validators=[   UniqueValidator(
                queryset=User.objects.all(),
                message='This username is already in use. Please choose a different username.'
            ),username_validator, min_length_validator, max_length_validator],  # Use the custom username and length validators
        help_text='Required. 30 characters or fewer. Start with a letter, and can contain letters, numbers, or underscores. Cannot start or end with an underscore.',
    )
    
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[password_validator],  # Use the custom password validator
    )

    class Meta:
        model = User
        fields = ['username', 'password'] 
   
    
    def create(self, validated_data):
        try:
            user = User.objects.create_user(
                username=validated_data['username'],
                password=validated_data['password']
            )
            return user
        except Exception as e:
            raise ValidationError(str(e))
    
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