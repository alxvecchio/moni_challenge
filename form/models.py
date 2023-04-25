# -*- coding: utf-8 -*-
"""Module that defines models for forms."""

from django.db import models


class Form(models.Model):
    """Class that represents a form."""

    dni = models.IntegerField()
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    amount_requested = models.FloatField(max_length=12)
    date = models.CharField(max_length=100)
    application_status = models.CharField(max_length=50, default=False)
