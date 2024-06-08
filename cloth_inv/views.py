from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Cloth


def index(request):
    clothes = Cloth.objects.all()
    return render(
        request,
        "base.html",
        {"clothes": clothes},  # context
    )
