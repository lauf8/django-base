from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    return render(request, "pages/index.html", {"segment": "index"})


def billing(request):
    return render(request, "pages/billing.html", {"segment": "billing"})


def tables(request):
    return render(request, "pages/tables.html", {"segment": "tables"})


def vr(request):
    return render(request, "pages/virtual-reality.html", {"segment": "vr"})


def rtl(request):
    return render(request, "pages/rtl.html", {"segment": "rtl"})


def profile(request):
    return render(request, "pages/profile.html", {"segment": "profile"})