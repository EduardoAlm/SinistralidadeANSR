import json

from django.utils import timezone
from rest_framework import serializers

from .models import utilizador


class utilizadorSerializer(serializers.Serializer):
    cc = serializers.IntegerField(required=True)
    nome = serializers.CharField(required=True)
    palavrapasse = serializers.CharField(required=True)
    ocupacao = serializers.CharField(required=True)
    n_distrito = serializers.CharField(required=True)

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
        user = utilizador(**validated_data)
        user.save()
        return user
