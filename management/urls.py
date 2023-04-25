# -*- coding: utf-8 -*-
"""Module for urls."""

from django.urls import path
from . import views


urlpatterns = [
    path("", views.management, name="management"),
    path("login/", views.login_manage, name="login_manage"),
    path("logout/", views.logout_user, name="logout"),
]
