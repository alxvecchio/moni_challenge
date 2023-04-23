# -*- coding: utf-8 -*-
"""Module that defines apps class."""

from django.apps import AppConfig


class HomeConfig(AppConfig):
    """Class for Config."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "home"
