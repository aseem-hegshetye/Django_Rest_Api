from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@g.com',
            password='aosidjaiojsd'
        )
        self.client.force_login(user=self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@g.com',
            password='123oaisjd'
        )

