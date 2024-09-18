from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('apps.home.urls')),
    path("admin/", admin.site.urls),
    path("", include('admin_soft.urls'))
]
