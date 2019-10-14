from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from .views import (
    HelloView,
    UserGetView,
    UserPostView
)

urlpatterns = [
    path('hello', HelloView.as_view(), name='hello'),
    path('user', UserPostView.as_view(), name='user'),
    url(r'^user/(?P<cc>.*)/$', UserGetView.as_view(), name='get_user'),
]
