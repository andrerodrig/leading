import json
from django.test import TestCase
from django.urls import reverse
from django.test import RequestFactory
from django.contrib.auth.models import User

from lead.models import Lead
from lead.serializers import LeadSerializer
from lead.resources import LeadViewSet


class LeadViewListTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.lead = Lead.objects.create(
            name="Doidão",
            email="doido@doido.com",
            message="Animal morto dos diabos"
        )

    def test_list_status_code_200(self):
        # Create a request of a GET request
        request = self.factory.get(reverse('leads-list'))
        response = LeadViewSet.as_view(
            actions={'get': 'list'}
        )(request)

        self.assertEqual(response.status_code, 200)

    def test_list_correct_format(self):
        # Compare the json data serializerd by the LeadSerializer
        # with the request.data
        leads = Lead.objects.all()
        lead_serializer = LeadSerializer(leads, many=True)
        request = self.client.get(reverse('leads-list'))
        self.assertEqual(lead_serializer.data, request.data)


class LeadViewCreateTestCase(TestCase):

    def setUp(self):
        User.objects.create_user(
            username='and', password='doidoido')

        self.factory = RequestFactory()
        self.new_lead = json.dumps({
            'name': 'Joao doido',
            'email': 'animal@gmail.com',
            'message': 'contact-me para prazer',
        })

    def test_create_returns_201(self):

        request = self.factory.post(
            reverse('leads-list'),
            self.new_lead,
            content_type='application/json'
        )
        response = LeadViewSet.as_view(
            actions={'post': 'create'}
        )(request)

        self.assertEqual(response.status_code, 201)
