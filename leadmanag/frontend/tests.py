from django.test import TestCase
from .views import index
from django.urls import reverse


class FrontendViewTestCase(TestCase):

    def test_index_page(self):
        url = reverse('index')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'frontend/index.html')
