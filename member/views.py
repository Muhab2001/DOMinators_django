from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from . import models

# Serializers define the API representation.
class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Membership
        fields = "__all__"


class CommitteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Committee
        fields = "__all__"


# ViewSets define the view behavior.
class MembershipViewSet(viewsets.ModelViewSet):
    queryset = models.Membership.objects.all()
    serializer_class = MembershipSerializer


class CommitteeViewSet(viewsets.ModelViewSet):
    queryset = models.Committee.objects.all()
    serializer_class = CommitteeSerializer
