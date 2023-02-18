from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import serializers, viewsets
import rest_framework
from rest_framework.permissions import IsAuthenticated

from . import models


class IsPresidentOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj: models.Invoice):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # permissions are only allowed to the president of the invoice's club.
        return obj.activity.club.president == request.user


# Serializers define the API representation.
class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Invoice
        fields = "__all__"

    def to_representation(self, instance):
        result = super().to_representation(instance)
        result["club"] = instance.activity.club.name
        result["supervisor"] = instance.activity.supervisor.username

        return result


class InvoiceViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated, IsPresidentOrReadOnly]

    def get_queryset(self):
        return [obj.invoice_set for obj in self.request.user.club.activity_set.all()]
