# -*- coding: utf-8 -*-
"""Module that defines apps class."""

from django.apps import AppConfig


class ManagementConfig(AppConfig):
    """Application for managing administration."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "management"
