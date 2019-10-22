from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

class HelloView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')


class UserGetView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None, cc=None):
        if id is not None:
            user = User.objects.filter(nr_cc=cc)
            serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

class UserPostView(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)