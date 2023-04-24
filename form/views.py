# -*- coding: utf-8 -*-
"""Module for views."""

from django.shortcuts import render

from django.http import HttpResponse
import logging

logger = logging.getLogger("prestamo_facil")


def form(request) -> HttpResponse:
    """Handle Home view and its requests.

    Args:
        request (HttpRequest): HTTP Request.

    Returns:
        HttpResponse: Renders home.html template with the given context.
    """
    try:
        logger.info(f'Entering form from {request.META["REMOTE_ADDR"]}')
        context: dict = {}
        return render(request, "form.html", context)
    except Exception as e:
        logger.error(f"Error: {e}")
