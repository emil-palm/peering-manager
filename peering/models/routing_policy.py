from django.urls import reverse
from django.db import models
from django.utils.safestring import mark_safe

from ..enums import (
    IPFamily,
    RoutingPolicyDirection,
    RoutingPolicyProtocol,
    RoutingPolicyType,
)

from peering_manager.models import OrganisationalModel


class RoutingPolicy(OrganisationalModel):
    direction = models.CharField(
        max_length=50,
        choices=RoutingPolicyDirection,
        default=RoutingPolicyDirection.IMPORT,
    )

    protocol = models.CharField(
        max_length=50,
        choices=RoutingPolicyProtocol,
        blank=True,
    )

    weight = models.PositiveSmallIntegerField(
        default=0, help_text="The higher the number, the higher the priority"
    )

    address_family = models.PositiveSmallIntegerField(
        default=IPFamily.ALL, choices=IPFamily
    )

    type = models.CharField(
        max_length=50,
        choices=RoutingPolicyType,
        default=RoutingPolicyType.PERMIT,
    )

    class Meta:
        verbose_name_plural = "routing policies"
        ordering = ["-weight", "name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("peering:routingpolicy_view", args=[self.pk])

    def get_direction_html(self, display_name=False):
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

    def get_protocol_html(self, display_name=False):
        if self.protocol == RoutingPolicyProtocol.BGP:
            badge_type = "badge-primary"
            text = self.get_protocol_display()
        elif self.protocol == RoutingPolicyProtocol.OSPF:
            badge_type = "badge-info"
            text = self.get_protocol_display()
        elif self.protocol == RoutingPolicyProtocol.ISIS:
            badge_type = "badge-dark"
            text = self.get_protocol_display()
        else:
            badge_type = "badge-secondary"
            text = "Unknown"

        if display_name:
            text = self.name

        return mark_safe(f'<span class="badge {badge_type}">{text}</span>')

    def get_type_html(self, display_name=False):
        if self.type == RoutingPolicyType.PERMIT:
            badge_type = "badge-success"
            text = self.get_type_display()
        else:
            badge_type = "badge-danger"
            text = self.get_type_display()

        if display_name:
            text = self.name

        return mark_safe(f'<span class="badge {badge_type}">{text}</span>')
