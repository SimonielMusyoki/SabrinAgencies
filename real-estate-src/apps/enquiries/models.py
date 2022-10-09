from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from apps.common.models import TimeStampedUUIDModel


class Enquiry(TimeStampedUUIDModel):
    name = models.CharField(_("Your Name"), max_length=200)
    phone_number = PhoneNumberField(
        _("Phone Number"),
        max_length=30,
        default="+254711000000",
    )
    email = models.EmailField(verbose_name=_("Email"))
    subject = models.CharField(max_length=100, verbose_name=_("Subject"))
    message = models.TextField(verbose_name=_("Message"))

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Enquiries"
