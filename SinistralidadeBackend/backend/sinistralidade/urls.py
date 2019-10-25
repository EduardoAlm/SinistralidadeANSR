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
    DistritoGetView,
    DistritoPostView,
    DistritoDeleteView,
    ConcelhoGetView,
    ConcelhoPostView,
    ConcelhoDeleteView,
    AcidenteGetView,
    AcidentePostView,
    AcidenteDeleteView
)

urlpatterns = [
    path('register/', UserPostView.as_view(), name='post_user'),
    path('registerdist/', DistritoPostView.as_view(), name='post_distrito'),
    path('registerconc/', ConcelhoPostView.as_view(), name='post_concelho'),
    path('registeracidente/', AcidentePostView.as_view(), name='post_acidente'),
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

]
