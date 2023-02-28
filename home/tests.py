from django.test import TestCase
from django.urls import reverse
from home.views import index
from pytest_django.asserts import assertTemplateUsed


class TestHome(TestCase):
    def test_get_home_page(self):
        uri = reverse(index)
        response = self.client.get(uri)
        assert response.status_code == 200
        assertTemplateUsed(response, "home/index.html")
        assert b"<h1>Welcome to Holiday Homes</h1>" in response.content
