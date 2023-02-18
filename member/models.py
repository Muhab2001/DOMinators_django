from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.translation import gettext as _

from base.models import Club


class MembershipKind(models.TextChoices):
    MEM = ("member", _("member"))
    CONT = ("cont", _("contributor"))


class Committee(models.Model):
    """A model to map a member to a coommittee in a club."""

    class Meta:
        verbose_name = _("committee")
        verbose_name_plural = _("committees")

    name = models.CharField(_("name"), max_length=100, default="")
    club = models.ForeignKey(Club, on_delete=models.CASCADE, verbose_name=_("club"))
    updated_on = models.DateTimeField(_("updated_on"), auto_now=True)
    supervisor = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_("supervisor")
    )


class Membership(models.Model):
    """A model represents the relationship from a user
    to a club"""

    class Meta:
        verbose_name = _("membership")
        verbose_name_plural = _("memberships")

    role = models.CharField(_("role"), max_length=50, blank=True)
    kind = models.CharField(_("kind"), max_length=50, choices=MembershipKind.choices)
    joined_on = models.DateTimeField(_("joined on"), auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("user"))
    committee = models.ForeignKey(
        Committee, on_delete=models.CASCADE, verbose_name=_("committee")
    )
