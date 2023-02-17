from django.urls import path, include
from rest_framework import routers

from . import views


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register("meberships", views.MembershipViewSet)
router.register("committees", views.CommitteeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
