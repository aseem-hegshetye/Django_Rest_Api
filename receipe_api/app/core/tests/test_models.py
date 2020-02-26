from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email(self):
        """ test if user can be created using email"""
        email = 'you@gmail.com'
        password = 'testpassword'
        user = get_user_model().objects.create_user(
            email= email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ test that the new email is normalized"""
        email='test@LONDON.COM'
        user=get_user_model().objects.create_user(email,'aoisdjoaisjd')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """" test with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'aosidjaosd')

    def test_create_new_super_user(self):
        """ test creating a new super user"""
        email = 'asdk@als.com'
        password = 'asdasodij'
        user = get_user_model().objects.create_super_user(
            email=email,
            password=password
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)