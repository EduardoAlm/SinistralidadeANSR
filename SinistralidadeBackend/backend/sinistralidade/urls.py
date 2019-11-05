from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from django.contrib.auth import views as auth_views

# from './SinistralidadeFrontend' import app

from .views import (
    UserGetView,
    UserPostView,
    UserDeleteView,
    UserGetAllView,
    UserUpdateView,
    DistritoGetView,
    DistritoPostView,
    DistritoDeleteView,
    ConcelhoGetView,
    ConcelhoPostView,
    ConcelhoDeleteView,
    ConcelhoGetAllView,
    ConcelhoGetDistView,
    AcidenteGetView,
    AcidentePostView,
    AcidenteDeleteView,
    AcidenteUpdateHospitalView,
    AcidenteGetIdView,
    AcidenteUpdateView,
    AcidenteGetLastID,
    HistoricoPostView,
    HistoricoGetLastId,
    HistoricoGetView,
)

urlpatterns = [
    path('register/', UserPostView.as_view(), name='post_user'),
    path('registerdist/', DistritoPostView.as_view(), name='post_distrito'),
    path('registerconc/', ConcelhoPostView.as_view(), name='post_concelho'),
    path('registeracidente/', AcidentePostView.as_view(), name='post_acidente'),
    path('acidenteuphospital/<int:id>/<int:mortos>/<int:feridosg>/<int:cc>/',
         AcidenteUpdateHospitalView.as_view(), name='update_acidentehospital'),
    path('acidenteid/<int:id>/',
         AcidenteGetIdView.as_view(), name='get_acidenteid'),

    path('userall/', UserGetAllView.as_view(), name='get_alluser'),
    url(r'^user/(?P<cc>.*)/$', UserGetView.as_view(), name='get_user'),
    url(r'^userdel/(?P<cc>.*)/$', UserDeleteView.as_view(), name='del_user'),
    url(r'^distrito/(?P<nome>.*)/$',
        DistritoGetView.as_view(), name='get_distrito'),
    url(r'^distritodel/(?P<nome>.*)/$',
        DistritoDeleteView.as_view(), name='del_distrito'),
    url(r'^concelho/(?P<nome>.*)/$', ConcelhoGetView.as_view(), name='get_concelho'),
    url(r'^concelhodel/(?P<nome>.*)/$',
        ConcelhoDeleteView.as_view(), name='del_concelho'),
    url(r'^acidente/(?P<concelho>.*)/$',
        AcidenteGetView.as_view(), name='get_acidente'),
    url(r'^acidentedel/(?P<id>.*)/$',
        AcidenteDeleteView.as_view(), name='del_acidente'),

    path('concelhoall/', ConcelhoGetAllView.as_view(), name='get_concelhoall'),
    url(r'^concelhodist/(?P<distrito>.*)/$',
        ConcelhoGetDistView.as_view(), name='get_concelhodist'),

    path('userupdate/<int:cc>/<str:nome>/<str:palavrapasse>/<str:ocupacao>/<str:n_distrito>/',
         UserUpdateView.as_view(), name='user_updateall'),
    path('acidenteupdate/<int:id>/<str:concelho>/<int:mortos>/<int:feridosg>/<str:via>/<str:km>/<str:natureza>/',
         AcidenteUpdateView.as_view(), name='update_acidente'),

    path('acidentelastid/', AcidenteGetLastID.as_view(), name='acidenteget_lastid'),

    path('historicopost/', HistoricoPostView.as_view(), name='post_historico'),

    path('historicogetlastid/', HistoricoGetLastId.as_view(),
         name='get_lastidhistorico'),

    path('historicoget/<int:id_acidente>/',
         HistoricoGetView.as_view(), name='get_historico')

]
