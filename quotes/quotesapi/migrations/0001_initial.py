# Generated by Django 3.0.4 on 2020-03-07 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('context', models.CharField(blank=True, max_length=200)),
                ('source', models.CharField(blank=True, max_length=200)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
