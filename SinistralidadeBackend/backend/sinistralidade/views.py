from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from .models import utilizador, distrito, concelho, acidente, historico
from .serializers import utilizadorSerializer, distritoSerializer, concelhoSerializer, acidenteSerializer, historicoSerializer
from django.db import connection
from django.db import transaction, DatabaseError
from django.http import JsonResponse
import datetime


# --------------------- DISTRITO FUNCTIONS------------------------------------------


class DistritoGetView(APIView):
    def get(self, request, format=None, nome=None):
        if nome is not None:
            dist = distrito.objects.filter(nome=nome)
            serializer = distritoSerializer(dist, many=True)
            print(serializer.data)
        return Response(serializer.data)


class DistritoPostView(APIView):
    @transaction.atomic
    def post(self, request, format=None):
        serializer = distritoSerializer(data=request.data)
        if serializer.is_valid():
            try:
                with transaction.atomic(using=None, savepoint=True):
                    serializer.save()
            except DatabaseError:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DistritoDeleteView(APIView):
    @transaction.atomic
    def post(self, request, nome=None):
        dist = distrito.objects.select_for_update().filter(nome=nome)
        try:
            with transaction.atomic(using=None, savepoint=True):
                dist.delete()
        except DatabaseError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
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
    @transaction.atomic
    def post(self, request, format=None):
        serializer = concelhoSerializer(data=request.data)
        if serializer.is_valid():
            try:
                with transaction.atomic(using=None, savepoint=True):
                    serializer.save()
            except DatabaseError:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConcelhoDeleteView(APIView):
    @transaction.atomic
    def post(self, request, nome=None):
        conc = concelho.objects.select_for_update().filter(nome=nome)
        try:
            with transaction.atomic(using=None, savepoint=True):
                conc.delete()
        except DatabaseError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
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
    @transaction.atomic
    def post(self, request, format=None):
        serializer = utilizadorSerializer(data=request.data)
        if serializer.is_valid():
            try:
                with transaction.atomic(using=None, savepoint=True):
                    serializer.save()
            except DatabaseError:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDeleteView(APIView):
    @transaction.atomic
    def post(self, request, cc=None):
        user = utilizador.objects.select_for_update().filter(cc=cc)
        try:
            with transaction.atomic(using=None, savepoint=True):
                user.delete()
        except DatabaseError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)


class UserUpdateView(APIView):
    @transaction.atomic
    def get(self, request, cc, nome, palavrapasse, ocupacao, n_distrito):
        user = utilizador.objects.select_for_update().filter(cc=cc)
        try:
            with transaction.atomic(using=None, savepoint=True):
                user.update(nome=nome, palavrapasse=palavrapasse,
                            ocupacao=ocupacao, n_distrito=n_distrito)
        except DatabaseError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
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
    @transaction.atomic
    def post(self, request, format=None):
        serializer = acidenteSerializer(data=request.data)
        if serializer.is_valid():
            try:
                with transaction.atomic(using=None, savepoint=True):
                    serializer.save()
            except DatabaseError:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AcidenteDeleteView(APIView):
    @transaction.atomic
    def post(self, request, id, format=None):
        acid = acidente.objects.select_for_update().get(id=id)
        try:
            with transaction.atomic(using=None, savepoint=True):
                acid.delete()
        except DatabaseError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)


class AcidenteUpdateHospitalView (APIView):
    @transaction.atomic
    def get(self, request, id, mortos, feridosg, cc):
        obj = acidente.objects.select_for_update().filter(id=id)
        lastID = historico.objects.latest('id')
        try:
            with transaction.atomic(using=None, savepoint=True):
                obj.update(mortos=mortos, feridosg=feridosg)
                # transaction.on_commit(chamar historico)
        except DatabaseError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)


class AcidenteUpdateView(APIView):
    def get(self, request, id, concelho, mortos, feridosg, via, km, natureza):
        obj = acidente.objects.select_for_update().filter(id=id)
        obj.update(concelho=concelho, mortos=mortos,
                   feridosg=feridosg, via=via, km=km, natureza=natureza)
        return Response(status=status.HTTP_200_OK)


class AcidenteGetLastID (APIView):
    def get(self, request):
        lastID = acidente.objects.latest('id')
        acid = acidente.objects.filter(id=lastID.id)
        serializer = acidenteSerializer(acid, many=True)
        return Response(serializer.data)


# --------------------------- Historico ------------------------------------------

class HistoricoGetView(APIView):

    def get(self, request, format=None, id_acidente=None):
        hist = historico.objects.filter(id_acidente=id_acidente)
        serializer = historicoSerializer(hist, many=True)
        return Response(serializer.data)


class HistoricoPostView (APIView):
    @transaction.atomic
    def post(self, request, format=None):
        serializer = historicoSerializer(data=request.data)
        if serializer.is_valid():
            try:
                with transaction.atomic(using=None, savepoint=True):
                    serializer.save()
            except DatabaseError:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HistoricoGetLastId (APIView):
    def get(self, request):
        try:
            lastID = historico.objects.latest('id')
        except historico.DoesNotExist:
            raise Http404("No historico matches the given query.")
        hist = historico.objects.filter(id=lastID.id)
        serializer = historicoSerializer(hist, many=True)
        return Response(serializer.data)
