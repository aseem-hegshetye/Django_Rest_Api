from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, AbstractUser
from django.conf import settings


class UserProfileManager(BaseUserManager):
    def create_user(self, email, full_name, first_name=None, password=None, **kwargs):
        """create new user"""
        if not email:
            raise ValueError('email required')

        email = self.normalize_email(email)
        user = self.model(email=email, full_name=full_name, password=password, first_name=first_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, first_name=None, password=None, **kwargs):
        user = self.create_user(email, full_name, first_name, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


# class UserProfile(AbstractBaseUser, PermissionsMixin):
#     """ User model """
#     username = models.EmailField(max_length=255, unique=True)
#     full_name = models.CharField(max_length=255)
#
#     objects = UserProfileManager()  # assigns a manager
#
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['full_name']
#
#     def get_full_name(self):
#         return self.full_name
#
#     def get_short_name(self):
#         return self.first_name
#
#     def __str__(self):
#         return self.email

class CustomUser(AbstractUser):
    """ just add phone field to existing user model"""
    phone = models.CharField(max_length=10)


class ProfileFeedItem(models.Model):
    user_profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ return model as string"""
        return self.status
