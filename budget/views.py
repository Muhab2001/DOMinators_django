from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from . import models

# Serializers define the API representation.
class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Invoice
        fields = "__all__"


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = models.Invoice.objects.all()
    serializer_class = InvoiceSerializer
