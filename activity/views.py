from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated

from . import models


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Activity
        fields = "__all__"


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Registration
        fields = "__all__"


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = models.Activity.objects.all()
    serializer_class = ActivitySerializer


class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = models.Activity.objects.all()
    serializer_class = RegistrationSerializer
