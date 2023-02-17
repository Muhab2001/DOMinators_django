from django.db import models
from django.db.models.query import django
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.translation import gettext as _


class UserProfile(models.Model):
    class Meta:
        verbose_name = _("user profile")
        verbose_name_plural = _("user profiles")

    # Connect to the django User object by on-to-one relation
    user = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)


class Club(models.Model):
    """A model represetns a club entity; its logo, header, name etc."""

    class Meta:
        verbose_name = _("club")
        verbose_name_plural = _("clubs")

    name = models.CharField(_("name"), max_length=50)
    logo = models.URLField(_("logo"), blank=True)
    header_image = models.URLField(_("header image"), blank=True)
    description = models.TextField(_("description"))
    theme = models.CharField(_("theme"), max_length=10)
    twitter_link = models.URLField(_("twitter link"), blank=True)

    president = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_("president")
    )


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
