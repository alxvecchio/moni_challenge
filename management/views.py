# -*- coding: utf-8 -*-
"""Module for views."""

import logging
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from form.models import Form

logger = logging.getLogger("prestamo_facil")


def login_manage(request) -> HttpResponse:
    """Login view for management staff. If user is already logged, redirects to management page.

    If user submits credentials and they are incorrect, shows error message and renders login page.

    Args:
        request (HttpRequest): HTTP Request.

    Returns:
        HttpResponse: Renders login_manage.html template.
    """
    logger.info(f'Entering Login to Management from {request.META["REMOTE_ADDR"]}')
    if request.user.is_staff:
        return redirect("management")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("management")
        else:
            messages.info(request, "El usuario o la contraseña es incorrecto")
    context: dict = {}
    return render(request, "login_manage.html", context)


def management(request) -> HttpResponse:
    """Render the management page with loan requests for authorized admin users.

    Args:
        request (HttpRequest): HTTP Request.

    Returns:
        HttpResponse: Renders management.html template with the requests loans.
    """
    logger.info(f'Entering Management from {request.META["REMOTE_ADDR"]}')
    if not request.user.is_staff:
        return HttpResponse("No tienes permiso para acceder a esta página")
    loans = Form.objects.all()
    return render(request, "management.html", {"loans": loans})


def logout_user(request) -> HttpResponse:
    """Log out the authenticated user and redirect to the home page.

    Args:
        request (HttpRequest): HTTP Request.

    Returns:
        HttpResponse: Redirect to home.
    """
    logout(request)
    return redirect("home")


def delete_loan(request, loan_id) -> HttpResponse:
    """Delete a request.

    Args:
        request (HttpRequest): HTTP Request.
        loan_id (int): id of the loan

    Returns:
        HttpResponse: Redirect to management.
    """
    try:
        loan = Form.objects.get(id=loan_id)
        loan.delete()  # Elimina el préstamo
        messages.success(request, "El préstamo ha sido eliminado exitosamente.")
    except Form.DoesNotExist:
        messages.error(
            request, "El préstamo no existe o ha sido eliminado previamente."
        )
    return redirect("management")
