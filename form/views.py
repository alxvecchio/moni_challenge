# -*- coding: utf-8 -*-
"""Module for views."""

import requests
import logging
import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from form.models import Form
from prestamo_facil.constants import STATUS_MSG, SUCCESS_MSG, MSG_ERROR


logger = logging.getLogger("prestamo_facil")


def form(request) -> HttpResponse:
    """Handle and create form view and its requests.

    Args:
        request (HttpRequest): HTTP Request.

    Returns:
        HttpResponse: Renders form.html template with the given context.
    """
    logger.info(f'Entering Form from {request.META["REMOTE_ADDR"]}')
    now = datetime.datetime.now().strftime("%d-%m-%Y - %H:%M:%S")
    if request.method == "POST":
        dni = request.POST.get("dni")
        name = request.POST.get("name")
        last_name = request.POST.get("last_name")
        gender = request.POST.get("gender")
        email = request.POST.get("email")
        amount_requested = request.POST.get("amount_requested")
        date = request.POST.get("date")
        # Validation of entered data
        if (
            not dni
            or not name
            or not last_name
            or not gender
            or not email
            or not amount_requested
        ):
            messages.info(request, "¡ERROR! - Hay un error en algún campo")
            return render(request, "form.html")
        # request to API
        response = requests.get(
            f"https://api.moni.com.ar/api/v4/scoring/pre-score/{dni}",
            headers={"credential": "ZGpzOTAzaWZuc2Zpb25kZnNubm5u"},
        )
        if response.status_code == 200:
            status = response.json().get("status")
            loan = Form.objects.get_or_create(
                dni=dni,
                name=name,
                last_name=last_name,
                gender=gender,
                email=email,
                amount_requested=amount_requested,
                date=now,
                application_status=status,
            )
            messages.info(request, SUCCESS_MSG + " " + STATUS_MSG + " " + status)
            return render(
                request,
                "form.html",
                {
                    "success_msg": SUCCESS_MSG,
                    "status_msg": STATUS_MSG,
                    "status": status,
                },
            )
        else:
            status = False
            messages.info(request, MSG_ERROR)
            return render(
                request, "form.html", {"msg_error": MSG_ERROR, "status": status}
            )

    return render(request, "form.html")
