from django.urls import path, include
from rest_framework import routers

from . import views


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register("users", views.UserViewSet)
router.register("clubs", views.ClubViewSet)
router.register("user_profile", views.ClubViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
