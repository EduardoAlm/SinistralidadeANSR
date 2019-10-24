from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from django.contrib.auth import views as auth_views

# from './SinistralidadeFrontend' import app

from .views import (
    HelloView,
    UserGetView,
    UserPostView,
    UserDeleteView,
    UserLogInView
)

urlpatterns = [
    path('hello', HelloView.as_view(), name='hello'),
    path('user', UserPostView.as_view(), name='post_user'),
    url(r'^user/(?P<cc>.*)/$', UserGetView.as_view(), name='get_user'),
    url(r'^userdel/(?P<cc>.*)/$', UserDeleteView.as_view(), name='del_user'),
    path('userlogin/', UserLogInView.as_view(), name='login'),
]
