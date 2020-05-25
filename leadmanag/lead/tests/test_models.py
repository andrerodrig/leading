from django.test import TestCase

from django.contrib.auth.models import User
from lead.models import Lead


class LeadTestCase(TestCase):

    def setUp(self):
        """Create a user for the tests"""
        self.user = User.objects.create_user(
            username="and", password="animalcomum"
        )

        Lead.objects.create(
            name="Testudo",
            email="testanimal@gmail.com",
            message="Some random stuff",
            owner=self.user
        )

    def test_return_str(self):
        lead1 = Lead.objects.get(name="Testudo")
        self.assertEqual(lead1.owner.username, 'and')
        self.assertEquals(lead1.__str__(), "Testudo")
