# -*- coding: utf-8 -*-
"""Module for urls."""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.form, name="form"),
]
