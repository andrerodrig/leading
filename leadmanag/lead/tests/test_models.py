from django.test import TestCase

from lead.models import Lead


class LeadTestCase(TestCase):

    def setUp(self):
        """Create a user for the tests"""
        Lead.objects.create(
            name="Testudo",
            email="testanimal@gmail.com",
            message="Some random stuff"
        )

    def test_return_str(self):
        lead1 = Lead.objects.get(name="Testudo")
        self.assertEquals(lead1.__str__(), "Testudo")
