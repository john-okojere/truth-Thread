from rest_framework import serializers, status
from .models import User
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from django.contrib.auth import get_user_model
User = get_user_model()

#Serializer to get Detail using Django Token Authentication
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators = [UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ("email","password","password2","username","first_name","last_name","phone","gender")
        extra_kwargs = {
            'first_name':{'required':True},
            'last_name': {'required':True}
        }
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {'Password':"Password field didn't match"}
            )
        return attrs
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()        
        return user