from django.urls import reverse
from django.db import models
from django.utils.safestring import mark_safe

from ..enums import IPFamily, RoutingPolicyDirection, RoutingPolicyProtocol

from peering_manager.models import OrganisationalModel


class RoutingPolicy(OrganisationalModel):
    direction = models.CharField(
        max_length=50,
        choices=RoutingPolicyDirection,
        default=RoutingPolicyDirection.IMPORT,
    )

    protocol = models.CharField(
        max_length=50, choices=RoutingPolicyProtocol, default=RoutingPolicyProtocol.BGP
    )

    weight = models.PositiveSmallIntegerField(
        default=0, help_text="The higher the number, the higher the priority"
    )
    address_family = models.PositiveSmallIntegerField(
        default=IPFamily.ALL, choices=IPFamily
    )

    class Meta:
        verbose_name_plural = "routing policies"
        ordering = ["-weight", "name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("peering:routingpolicy_view", args=[self.pk])

    def get_type_html(self, display_name=False):
        if self.direction == RoutingPolicyDirection.EXPORT:
            badge_type = "badge-primary"
            text = self.get_direction_display()
        elif self.direction == RoutingPolicyDirection.IMPORT:
            badge_type = "badge-info"
            text = self.get_direction_display()
        elif self.direction == RoutingPolicyDirection.IMPORT_EXPORT:
            badge_type = "badge-dark"
            text = self.get_direction_display()
        else:
            badge_type = "badge-secondary"
            text = "Unknown"

        if display_name:
            text = self.name

        return mark_safe(f'<span class="badge {badge_type}">{text}</span>')
