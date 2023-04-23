# -*- coding: utf-8 -*-
"""Module that defines apps class."""

from django.apps import AppConfig


class FormConfig(AppConfig):
    """Config for creating forms."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "form"
