# -*- coding: utf-8 -*-
"""Module for views."""

from django.http import HttpResponse
from django.shortcuts import render


def home(request) -> HttpResponse:
    """Handle Home view and its requests.

    Args:
        request (HttpRequest): HTTP Request.

    Returns:
        HttpResponse: Renders home.html template with the given context.
    """
    context: dict = {}
    return render(request, "home.html", context)
