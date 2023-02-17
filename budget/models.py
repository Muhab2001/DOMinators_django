"""
All models related to club's budget,
    - Invoice
"""

from django.db import models
from django.utils.translation import gettext as _

from activity.models import Activity


class Invoice(models.Model):
    """A model represents an invoice payment related to
    an activity"""

    class Meta:
        verbose_name = _("invoice")
        verbose_name_plural = _("invoices")

    amount = models.FloatField(_("amount"))
    seller = models.CharField(_("seller"), max_length=100)
    date = models.DateField(_("date"))
    number = models.IntegerField(_("number"))
    description = models.CharField(_("description"), max_length=200)
    updated_on = models.DateTimeField(_("updated_on"), auto_now=True)
    added_on = models.DateTimeField(_("added on"), auto_now_add=True)

    activity = models.ForeignKey(
        Activity, on_delete=models.CASCADE, verbose_name=_("activity")
    )
