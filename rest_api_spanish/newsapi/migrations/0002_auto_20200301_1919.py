# Generated by Django 3.0.3 on 2020-03-01 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='auther',
            new_name='author',
        ),
    ]
