# Generated by Django 3.0.3 on 2020-02-20 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_userprofilefield'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfileField',
            new_name='ProfileFeedItem',
        ),
    ]
