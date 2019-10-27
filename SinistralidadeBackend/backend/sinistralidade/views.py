from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from .models import utilizador, distrito, concelho, acidente
from .serializers import utilizadorSerializer, distritoSerializer, concelhoSerializer, acidenteSerializer
from django.db import connection
from django.db import transaction

# --------------------- DISTRITO FUNCTIONS------------------------------------------


class DistritoGetView(APIView):
    def get(self, request, format=None, nome=None):
        if nome is not None:
            dist = distrito.objects.filter(nome=nome)
            serializer = distritoSerializer(dist, many=True)
            print(serializer.data)
        return Response(serializer.data)


class DistritoPostView(APIView):

    def post(self, request, format=None):
        serializer = distritoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DistritoDeleteView(APIView):

    def delete(self, request, nome=None):
        dist = distrito.objects.filter(nome=nome)
        dist.delete()
        return Response(status=status.HTTP_200_OK)


# -----------------------CONCELHO FUNCTIONS-----------------------------------------


class ConcelhoGetView(APIView):
    def get(self, request, format=None, nome=None):
        if nome is not None:
            conc = concelho.objects.filter(nome=nome)
            serializer = concelhoSerializer(conc, many=True)
            print(serializer.data)
        return Response(serializer.data)


class ConcelhoGetDistView(APIView):
    def get(self, request, format=None, distrito=None):
        conc = concelho.objects.filter(n_distrito=distrito)
        serializer = concelhoSerializer(conc, many=True)
        print(serializer.data)
        return Response(serializer.data)


class ConcelhoGetAllView(APIView):
    def get(self, request, format=None):
        conc = concelho.objects.all()
        serializer = concelhoSerializer(conc, many=True)
        return Response(serializer.data)


class ConcelhoPostView(APIView):

    def post(self, request, format=None):
        serializer = concelhoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConcelhoDeleteView(APIView):

    def delete(self, request, nome=None):
        conc = concelho.objects.filter(nome=nome)
        conc.delete()
        return Response(status=status.HTTP_200_OK)


# ----------------------------------USER FUNCTIONS--------------------------------


class UserGetView(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None, cc=None):
        if id is not None:
            user = utilizador.objects.filter(cc=cc)
            serializer = utilizadorSerializer(user, many=True)
            print(serializer.data)
        return Response(serializer.data)


class UserGetAllView(APIView):
    def get(self, request, format=None, cc=None):
        users = utilizador.objects.all()
        serializer = utilizadorSerializer(users, many=True)
        return Response(serializer.data)


class UserPostView(APIView):

    def post(self, request, format=None):
        serializer = utilizadorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDeleteView(APIView):

    def delete(self, request, cc=None):
        user = utilizador.objects.filter(cc=cc)
        user.delete()
        return Response(status=status.HTTP_200_OK)

# ------------------------------------ACIDENTE FUNCTIONS------------------------------


class AcidenteGetView(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None, concelho=None):
        acid = acidente.objects.filter(concelho=concelho)
        serializer = acidenteSerializer(acid, many=True)
        return Response(serializer.data)


class AcidenteGetIdView(APIView):
    def get(self, request, format=None, id=None):
        acid = acidente.objects.filter(id=id)
        serializer = acidenteSerializer(acid, many=True)
        return Response(serializer.data)


class AcidentePostView(APIView):

    def post(self, request, format=None):
        serializer = acidenteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AcidenteDeleteView(APIView):
    def delete(self, request, id, format=None):
        acid = acidente.objects.filter(id=id)
        acid.delete()
        return Response(status=status.HTTP_200_OK)


class AcidenteUpdateView (APIView):
    def get(self, request, id, mortos, feridosg):
        obj = acidente.objects.filter(id=id)
        obj.update(mortos=mortos, feridosg=feridosg)
        return Response(status=status.HTTP_200_OK)
