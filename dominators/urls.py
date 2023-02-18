"""dominators URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

import base.views
import member.views
import budget.views
import activity.views

router = routers.DefaultRouter()

router.register("meberships", member.views.MembershipViewSet)
router.register("committees", member.views.CommitteeViewSet)
router.register("invoices", budget.views.InvoiceViewSet, basename="invoice")
router.register("users", base.views.UserViewSet)
router.register("clubs", base.views.ClubViewSet)
router.register("user_profile", base.views.UserProfileViewSet)
router.register("activities", activity.views.ActivityViewSet)
router.register("registrations", activity.views.RegistrationViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/me/", base.views.MeUserView.as_view()),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
