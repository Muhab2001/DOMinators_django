from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.translation import gettext as _
from cloudinary.models import CloudinaryField


class UserProfile(models.Model):
    class Meta:
        verbose_name = _("user profile")
        verbose_name_plural = _("user profiles")

    # Connect to the django User object by on-to-one relation
    user = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
    profile_pic = CloudinaryField(
        _("profile picture"),
        default="image/upload/v1676716777/qe8vfjfudtc8pti3iz3l.png",
    )


class Club(models.Model):
    """A model represetns a club entity; its logo, header, name etc."""

    class Meta:
        verbose_name = _("club")
        verbose_name_plural = _("clubs")

    name = models.CharField(_("name"), max_length=50)
    logo = CloudinaryField(
        _("logo"), default="image/upload/v1676716777/qe8vfjfudtc8pti3iz3l.png"
    )
    header_image = CloudinaryField(
        _("header image"), default="image/upload/v1676716777/qe8vfjfudtc8pti3iz3l.png"
    )
    description = models.TextField(_("description"))
    theme = models.CharField(_("theme"), max_length=10)
    twitter_link = models.URLField(_("twitter link"), blank=True, default="")
    facebook_link = models.URLField(_("twitter link"), blank=True, default="")
    instagram_link = models.URLField(_("twitter link"), blank=True, default="")

    president = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name=_("president")
    )


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
