import json

from django.utils import timezone
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.Serializer):
    nr_cc = serializers.CharField(required=True)
    username = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    distrito =  serializers.CharField(required=True)

    def update(self, instance, validated_data):
        """
        Override
        """
        print("This is an update.")
        pass

    def validate(self, attrs):
        """
        Validate the model attributes
        """
        for attr in attrs:
            print(attr)
        return attrs

    
    def create(self, validated_data):
        """
        Create the model object
        """
        user = User(**validated_data)
        user.save()
        return user

    

