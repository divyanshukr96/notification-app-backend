# Generated by Django 2.2.5 on 2019-09-20 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_auto_20190918_1526'),
    ]

    operations = [
        migrations.CreateModel(
            name='Society',
            fields=[
                ('user', models.OneToOneField(limit_choices_to={'user_type': 'FACULTY'}, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='society_user', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('registration_number', models.CharField(max_length=20, null=True)),
                ('faculty_advisor', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]