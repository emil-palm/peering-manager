from django.urls import reverse
from django.db import models
from django.utils.safestring import mark_safe

from ..enums import BGPState, CommunityType, DeviceStatus, IPFamily, RoutingPolicyType
from peering_manager.models import OrganisationalModel


class RoutingPolicy(OrganisationalModel):
    type = models.CharField(
        max_length=50,
        choices=RoutingPolicyType,
        default=RoutingPolicyType.IMPORT,
    )
    weight = models.PositiveSmallIntegerField(
        default=0, help_text="The higher the number, the higher the priority"
    )
    address_family = models.PositiveSmallIntegerField(
        default=IPFamily.ALL, choices=IPFamily
    )
    communities = models.ManyToManyField("Community", blank=True)

    class Meta:
        verbose_name_plural = "routing policies"
        ordering = ["-weight", "name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("peering:routingpolicy_view", args=[self.pk])

    def get_type_html(self, display_name=False):
        if self.type == RoutingPolicyType.EXPORT:
            badge_type = "badge-primary"
            text = self.get_type_display()
        elif self.type == RoutingPolicyType.IMPORT:
            badge_type = "badge-info"
            text = self.get_type_display()
        elif self.type == RoutingPolicyType.IMPORT_EXPORT:
            badge_type = "badge-dark"
            text = self.get_type_display()
        else:
            badge_type = "badge-secondary"
            text = "Unknown"

        if display_name:
            text = self.name

        return mark_safe(f'<span class="badge {badge_type}">{text}</span>')
