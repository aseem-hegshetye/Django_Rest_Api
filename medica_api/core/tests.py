import json
# from django.conf.settings import AUTH_USER_MODEL
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from core.serializers import CustomUserSerializer
from .urls import *
from .models import *


class CustomUserTest(APITestCase):
    """
        test everythin about custom user
    """

    @classmethod
    def setUpTestData(cls):
        cls.user1 = CustomUser.objects.create(
            username='testuser',
            password='oaisdoaijsd',
            first_name='testuser',
            last_name='rajula'
        )

    def test_signup(self):
        """ test creating new user"""
        response = self.client.post('/user/', {
            'username': 'aseem123', 'password': 'passwrodaosida123'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_another_user(self):
        """ user should not be able to update another user"""
        user1_response = self.client.post(reverse('user-list'), {
            'username': 'aseem', 'password': 'passwrodaosida123'
        })
        update_user_resp = self.client.patch(
            reverse('user-list') + '1/', {
                'username': 'rakesh', 'password': 'passwrodaosida123'
            })

        self.assertEqual(update_user_resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_request_should_not_work(self):
        """ get all users should not work"""
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_detail_requests_after_authentication(self):
        """ get request should work after auth"""
        print(f'cls.user1={self.user1}')
        user_detail_url = reverse('user-detail',kwargs={'pk':1})
        self.token = Token.objects.create(user=self.user1)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token.key)
        response = self.client.get(user_detail_url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

        response_patch = self.client.patch(user_detail_url,{
            'username': 'random_user', 'password': 'passwrodaosida123'
        })
        print(f'response_patch data={response_patch.data}')
        self.assertEqual(response_patch.data,
                         {'id': 1, 'username': 'random_user', 'first_name': 'testuser', 'last_name': 'rajula', 'email': ''})
        self.assertEqual(response_patch.status_code,status.HTTP_200_OK)

        response = self.client.get(user_detail_url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data['username'],'random_user')
