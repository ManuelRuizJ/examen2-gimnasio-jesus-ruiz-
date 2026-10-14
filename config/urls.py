from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("gimnasio.api_urls")),
    path("", include("gimnasio.urls")),
]
