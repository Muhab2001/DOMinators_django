"""All models related to Activity Management of clubs
    - Activiy
"""

from django.db import models
from django.db.models.query import django
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.translation import gettext as _

from base.models import Club


class Activity(models.Model):
    """A models represets an activity entity for a club."""

    class Meta:
        verbose_name = _("activity")
        verbose_name_plural = _("activities")

    title = models.CharField(_("title"), max_length=100)
    location = models.CharField(_("location"), max_length=100)
    updated_on = models.DateTimeField(_("updated on"), auto_now=True)
    location_link = models.URLField(_("location link"), blank=True)
    front_image = models.URLField(_("front image"), blank=True)
    attendance_max = models.IntegerField(_("attendance max"))
    description = models.TextField(_("description"))

    supervisor = models.ForeignKey(
        Club, on_delete=models.CASCADE, verbose_name="supervisor"
    )


class RegistrationEnum(models.TextChoices):
    REG = ("register", _("register"))
    ATTEND = ("attend", _("attendance"))


class Registration(models.Model):
    """A model represents a non-logged in user, willing to
    register in an Activity, or confirming attendance."""

    class Meta:
        verbose_name = _("registration")
        verbose_name_plural = _("registrations")

    name = models.CharField(_("name"), max_length=100)
    email = models.EmailField(_("email"))
    added_on = models.DateTimeField(_("added on"), auto_now=True)
    kind = models.CharField(_("kind"), max_length=50, choices=RegistrationEnum.choices)

    activity = models.ForeignKey(
        Activity, on_delete=models.CASCADE, verbose_name=_("activity")
    )
