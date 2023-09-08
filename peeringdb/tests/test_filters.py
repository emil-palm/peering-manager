from django.test import TestCase
from django.utils import timezone

from ..filtersets import *
from ..models import *


class SynchronisationTestCase(TestCase):
    queryset = Synchronisation.objects.all()
    filterset = SynchronisationFilterSet

    @classmethod
    def setUpTestData(cls):
        cls.times = [timezone.now(), timezone.now(), timezone.now()]
        Synchronisation.objects.bulk_create(
            [
                Synchronisation(time=cls.times[0], created=1, updated=0, deleted=0),
                Synchronisation(time=cls.times[1], created=0, updated=1, deleted=0),
                Synchronisation(time=cls.times[2], created=0, updated=0, deleted=1),
            ]
        )

    def test_time(self):
        params = {"time": self.times[0]}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_created(self):
        params = {"created": 1}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)
        params = {"created": 0}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)

    def test_updated(self):
        params = {"updated": 1}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)
        params = {"updated": 0}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)

    def test_deleted(self):
        params = {"deleted": 1}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)
        params = {"deleted": 0}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 2)
