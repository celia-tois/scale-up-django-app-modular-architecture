import pytest
from django.test import TestCase
from django.urls import reverse
from profiles.views import index, profile
from profiles.models import Profile
from django.contrib.auth.models import User
from pytest_django.asserts import assertTemplateUsed


class TestProfiles(TestCase):
    def test_get_list_page(self):
        uri = reverse(index)
        response = self.client.get(uri)
        assert response.status_code == 200
        assertTemplateUsed(response, "profiles/index.html")
        assert b"<h1>Profiles</h1>" in response.content

    @pytest.mark.django_db
    def test_get_instance_page(self):
        user_instance = User.objects.create(username="Test user")
        profile_instance = Profile.objects.create(
            user=user_instance,
            favorite_city="London",
        )
        uri = reverse(profile, kwargs={"username": profile_instance})
        response = self.client.get(uri)
        assert response.status_code == 200
        assertTemplateUsed(response, "profiles/profile.html")
        assert b"<h1>Test user</h1>" in response.content
