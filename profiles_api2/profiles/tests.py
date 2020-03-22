import json
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from profiles.api.serializers import ProfileSerializer
from profiles.models import Profile

from profiles.models import *
from profiles.api.serializers import *


# class RegistrationTestCase(APITestCase):
#     def test_registration(self):
#         data = {
#             "username": "testcase2",
#             "email": "awersj@gmail.com",
#             "password1": "asodiOASS09123019&&&&",
#             "password2": "asodiOASS09123019&&&&"
#         }
#         response = self.client.post("/api/rest-auth/registration/", data=data)
#         print(response.data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         # 18de436342af65c3e3438d9e71ad1b8489847f61


# class ProfileViewSetTest(APITestCase):
#     """
#     API based authentication, can be used from other mobile app too
#     """
#     @classmethod
#     def setUpTestData(cls):
#         cls.user = User.objects.create_user(
#             username="user1",
#             email="awersj@gmail.com",
#             password="jliajsdOIJ9878ajj123"
#         )
#         profile = Profile.objects.get(user=cls.user)
#         profile.bio = 'nothing special'
#         profile.city = 'nashik'
#         profile.save()
#
#         cls.user2 = User.objects.create_user(
#             username="user2",
#             email="oaisjdoa@gmail.com",
#             password="jliajsdOIJ9878ajj"
#         )
#
#     def setUp(self):
#         data = {
#             "username": self.user2.username,
#             "email": self.user2.email,
#             "password": 'jliajsdOIJ9878ajj'  # dont use cls.user.password coz its hashed
#         }
#
#         # login
#         response = self.client.post(
#             '/api/rest-auth/login/', data
#         )
#         self.key = response.get('key')
#         print('setup response=', response.data)
#
#     def test_profiles_list(self):
#         reverse_profiles2 = reverse('profiles2-list')
#         print(f'reverse_profiles2={reverse_profiles2}')
#         response = self.client.get(reverse_profiles2)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_profiles_detail_loggedin_user(self):
#         # read only
#         response = self.client.get('/api/profiles2/1/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#         # put should work
#         response = self.client.put(
#             '/api/profiles2/1/',
#             data={'city': 'ahmadabad'})
#         print(f'response data={response.data}, code = {response.status_code}')
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#
#     def test_profiles_detail_foreign_user(self):
#         # read only should work
#         response = self.client.get('/api/profiles2/2/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#         # put should not work
#         response = self.client.put(
#             '/api/profiles2/2/',
#             data={'city': 'ahmadabad'})
#         print(f'response data={response.data}, code = {response.status_code}')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

class ProfilesViewSetTestCase(APITestCase):
    """
    Django specific token based authentication. No API authentication used
    """

    def setUp(self):
        self.user = User.objects.create_user(username='user1',
                                             password='oiloon123')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_profile_list_authenticated(self):
        response = self.client.get(reverse('profiles2-list'))
        print('profiles list resp = ', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(reverse('profiles2-list'))
        print('profiles list resp = ', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_detail_retrieve_authenticated(self):
        response = self.client.get(reverse("profiles2-detail",
                                           kwargs={'pk': 1}))
        self.assertEqual(response.data['user'], 'user1')

    def test_update_profile(self):
        response = self.client.put(reverse('profiles2-detail',
                                           kwargs={'pk': 1}), {'bio': 'no bio'})
        print(f'response = {response.data}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_profile_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.put(reverse('profiles2-detail',
                                           kwargs={'pk': 1}), {'bio': 'no bio'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class ProfilesViewStatusTestCase(APITestCase):
    list_url = reverse('status-list')

    def setUp(self):
        self.user = User.objects.create_user(username='user1',
                                             password='asdlkjasdklj123')
        self.status = ProfileStatus.objects.create(
            user_profile=self.user.profile,
            status_content="love life"
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_status_list(self):
        response = self.client.get(reverse("status-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_status_detail(self):
        response = self.client.get(reverse("status-detail",
                                           kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = ProfileStatusSerializer(instance=self.status)
        status_content = serializer.data.get('status_content')
        self.assertEqual(status_content, response.data.get('status_content'))

    def test_put_status_by_authorized_user(self):
        response = self.client.put(reverse("status-detail",
                                           kwargs={'pk': 1}),
                                   {'status_content': 'new status'})
        print(f'response={response.data}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('status_content'), 'new status')

    def test_status_create(self):
        data = {"status_content": "new f status"}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_status_by_unauthorized_user(self):
        user2 = User.objects.create_user(username='user2',
                                         password='ajsd09au0uqwe9')
        self.client.force_authenticate(user=user2)

        response = self.client.put(reverse("status-detail",
                                           kwargs={'pk': 1}),
                                   {'status_content': 'new status'})
        print(f'response={response.data}')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
