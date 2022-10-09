from io import open_code
from django.db import models
from django.utils.translation import gettext_lazy as _

from real_estate.settings.base import AUTH_USER_MODEL
from apps.common.models import TimeStampedUUIDModel
from apps.profiles.models import Profile


class Rating(TimeStampedUUIDModel):
    class Range(models.IntegerChoices):
        RATING_1 = 1, _("Poor")
        RATING_2 = 2, _("Fair")
        RATING_3 = 3, _("Average")
        RATING_4 = 4, _("Good")
        RATING_5 = 5, _("Excellent")

    rated_by = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name=_("User providing the rating"),
        on_delete=models.SET_NULL,
        null=True,
    )
    agent = models.ForeignKey(
        Profile,
        verbose_name=_("Agent being Rated"),
        on_delete=models.SET_NULL,
        null=True,
        related_name="agent_review",
    )

    rating = models.IntegerField(
        verbose_name=_("Rating"),
        choices=Range.choices,
        help_text="1-Poor, 2-Fair, 3-Average, 4-Good, 5-Excellent",
        default=0,
    )

    comment = models.TextField(verbose_name=_("Comment"))

    class Meta:
        unique_together = ["rated_by", "agent"]

    def __str__(self) -> str:
        return f"{self.agent} rated at {self.rating}"
