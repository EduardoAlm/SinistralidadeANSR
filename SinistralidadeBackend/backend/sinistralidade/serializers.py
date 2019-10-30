import json

from django.utils import timezone
from rest_framework import serializers

from .models import utilizador, distrito, concelho, acidente, historico


class distritoSerializer(serializers.Serializer):
    nome = serializers.CharField(required=True)

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
        dist = distrito(**validated_data)
        dist.save()
        return dist


class concelhoSerializer(serializers.Serializer):
    nome = serializers.CharField(required=True)
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
        conc = concelho(**validated_data)
        conc.save()
        return conc


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


class acidenteSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    concelho = serializers.CharField(required=True)
    datahora = serializers.DateTimeField(required=True)
    mortos = serializers.IntegerField(required=True)
    feridosg = serializers.IntegerField(required=True)
    via = serializers.CharField(required=True)
    km = serializers.CharField(required=True)
    natureza = serializers.CharField(required=True)

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
        aciden = acidente(**validated_data)
        aciden.save()
        return aciden


class historicoSerializer (serializers.Serializer):
    id = serializers.IntegerField()
    datahora = serializers.DateTimeField()
    cc_user = serializers.IntegerField()
    id_acidente = serializers.IntegerField()

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
        hist = historico(**validated_data)
        hist.save()
        return hist
