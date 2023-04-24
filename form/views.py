# -*- coding: utf-8 -*-
"""Module for views."""

import requests
import logging
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from form.models import Form


logger = logging.getLogger("prestamo_facil")


def form(request) -> HttpResponse:
    """Handle and create form view and its requests.

    Args:
        request (HttpRequest): HTTP Request.

    Returns:
        HttpResponse: Renders form.html template with the given context.
    """
    if request.method == "POST":
        dni = request.POST.get("dni")
        name = request.POST.get("name")
        last_name = request.POST.get("last_name")
        gender = request.POST.get("gender")
        email = request.POST.get("email")
        amount_requested = request.POST.get("amount_requested")
        # Validation of entered data
        if (
            not dni
            or not name
            or not last_name
            or not gender
            or not email
            or not amount_requested
        ):
            print("uooohh", dni, type(dni))
            print("nombre", name, last_name, gender, email, amount_requested)
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
                application_status=status,
            )
            success_msg = "Solicitud registrada con éxito"
            status_msg = "Estado de la solicitud:"
            messages.info(request, success_msg + " " + status_msg + " " + status)
            return render(
                request,
                "form.html",
                {
                    "success_msg": success_msg,
                    "status_msg": status_msg,
                    "status": status,
                },
            )
        else:
            print("BUUUUUUUUUH")
            status = False
            msg_error = "¡ERROR! - La solicitud no pudo ser registrada"
            messages.info(request, msg_error)
            return render(
                request, "form.html", {"msg_error": msg_error, "status": status}
            )

    return render(request, "form.html")
