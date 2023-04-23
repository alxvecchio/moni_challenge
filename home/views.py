# -*- coding: utf-8 -*-
"""Module for views."""

from django.http import HttpResponse
from django.shortcuts import render
import logging

logger = logging.getLogger("prestamo_facil")


def home(request) -> HttpResponse:
    """Handle Home view and its requests.

    Args:
        request (HttpRequest): HTTP Request.

    Returns:
        HttpResponse: Renders home.html template with the given context.
    """
    try:
        logger.info(f'Entering Home from {request.META["REMOTE_ADDR"]}')
        context: dict = {}
        return render(request, "home.html", context)
    except Exception as e:
        logger.error(f"Error: {e}")
