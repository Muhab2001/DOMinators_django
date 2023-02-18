import cloudinary
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from cloudinary.uploader import upload


from . import models


def upload_image(file, name):

    # Upload the image and get its URL
    # ==============================

    # Upload the image.
    # Set the asset's public ID and allow overwriting the asset with new versions
    upload(
        file,
        public_id=name,
        unique_filename=False,
        overwrite=True,
    )

    # Build the URL for the image and save it in the variable 'srcURL'
    src_url = cloudinary.CloudinaryImage(name).build_url()

    # Log the image URL to the console.
    # Copy this URL in a browser tab to generate the image on the fly.
    print("****2. Upload an image****\nDelivery URL: ", src_url, "\n")


class IsPresidentOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj: models.Club):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        # permissions are only allowed to the president of the invoice's club.
        return obj.president == request.user


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "is_staff"]


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Club
        fields = "__all__"
        read_only_fields = ["president", "image"]

    def to_representation(self, instance):
        result = super().to_representation(instance)
        result["image"] = instance.image.url

        return result


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = "__all__"


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ClubViewSet(viewsets.ModelViewSet):
    queryset = models.Club.objects.all()
    serializer_class = ClubSerializer
    permission_classes = [IsPresidentOrReadOnly]

    def perform_update(self, serializer):
        if serializer.context["request"].FILES:
            file = serializer.context["request"].FILES["file"]
            serializer.validated_data["image"] = file

        super().perform_update(serializer)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = models.UserProfile.objects.all()
    serializer_class = UserProfileSerializer
