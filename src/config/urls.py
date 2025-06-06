"""
URL configuration for PetHotel project.

"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


from core.views import HomeView

urlpatterns = [
    path("admin/", admin.site.urls),

    # user accounts and profiles management
    path(
        "users/",
        include("users.urls")
    ),

    # OpenAPI-related views
    path(
        "api-schema/",
        include("core.api-schema.urls")
    ),

    # homepage
    path("", HomeView.as_view(), name="home")
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
