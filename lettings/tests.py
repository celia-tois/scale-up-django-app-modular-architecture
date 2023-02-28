import pytest
from django.test import TestCase
from django.urls import reverse
from lettings.views import index, letting
from lettings.models import Letting, Address
from pytest_django.asserts import assertTemplateUsed


class TestLettings(TestCase):
    def test_get_list_page(self):
        uri = reverse(index)
        response = self.client.get(uri)
        assert response.status_code == 200
        assertTemplateUsed(response, "lettings/index.html")
        assert b"<h1>Lettings</h1>" in response.content

    @pytest.mark.django_db
    def test_get_instance_page(self):
        address_instance = Address.objects.create(
            number=4290,
            street="Rockwell Lane",
            city="Kinston",
            state="NC",
            zip_code=28501,
            country_iso_code="840"
            )
        letting_instance = Letting.objects.create(
            title="Family house",
            address=address_instance,
        )
        uri = reverse(letting, kwargs={"letting_id": letting_instance.id})
        response = self.client.get(uri)
        assert response.status_code == 200
        assertTemplateUsed(response, "lettings/letting.html")
        assert b"<h1>Family house</h1>" in response.content
