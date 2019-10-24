from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from .models import utilizador
from .serializers import utilizadorSerializer


class UserGetView(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None, cc=None, palavrapasse=None):
        if id is not None:
            user = utilizador.objects.filter(cc=cc)
            serializer = utilizadorSerializer(user, many=True)
            print(serializer.data)
        return Response(serializer.data)


class UserPostView(APIView):

    def post(self, request, format=None):
        serializer = utilizadorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDeleteView(APIView):

    def destroy(self, request, cc=None):
        user = utilizador.objects.filter(cc=cc)
        user.delete()
        return Response(status=status.HTTP_200_OK)
