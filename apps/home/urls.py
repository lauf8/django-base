from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("billing/", views.billing, name="billing"),
    path("tables/", views.tables, name="tables"),
    path("vr/", views.vr, name="vr"),
    path("rtl/", views.rtl, name="rtl"),
    path("profile/", views.profile, name="profile"),
]
