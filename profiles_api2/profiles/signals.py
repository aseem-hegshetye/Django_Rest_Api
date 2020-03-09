from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from profiles.models import Profile


@receiver(signal=post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    As soon as new User is created & saved, we create a new Profile instance
    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return:
    """
    print(f'created={created}')
    if created:
        Profile.objects.create(user=instance)
