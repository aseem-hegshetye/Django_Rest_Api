from django.db import models

from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Instead of extending abstractuser class, we are creating new model
    and mapping it onetoone to User model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=240, blank=True)
    city = models.CharField(max_length=30, blank=True)
    avatar = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class ProfileStatus(models.Model):
    """
    one profile can have multiple status
    """
    user_profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    status_content = models.CharField(max_length=240)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        # instead of showing ProfileStatuss in admin console we now show statuses
        verbose_name_plural = 'statuses'

    def __str__(self):
        return str(self.user_profile)