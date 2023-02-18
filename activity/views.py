from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import serializers, viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from urllib3.util.retry import email
from base.models import Club
from . import models


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Activity
        fields = "__all__"

    def to_representation(self, instance):
        result = super().to_representation(instance)

        result["image"] = instance.image.url
        result["count"] = instance.registration_set.count()
        return result


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Registration
        fields = "__all__"


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = models.Activity.objects.all()
    serializer_class = ActivitySerializer


class ClubActivityView(ListAPIView):
    serializer_class = ActivitySerializer

    def get_queryset(self):
        print(self.request, self.kwargs)

        return Club.objects.get(pk=self.kwargs["pk"]).activity_set.all()


class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = models.Registration.objects.all()
    serializer_class = RegistrationSerializer

    def perform_create(self, serializer):

        serializer.save(name="", email="", kind=models.RegistrationEnum.ATTEND)
