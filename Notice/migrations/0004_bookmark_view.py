# Generated by Django 2.2.5 on 2019-10-12 16:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Notice', '0003_notice_visible'),
    ]

    operations = [
        migrations.CreateModel(
            name='View',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.TextField(verbose_name='device id')),
                ('device_name', models.TextField(null=True, verbose_name='device name')),
                ('platform', models.CharField(max_length=50, verbose_name='device platform')),
                ('notice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Notice.Notice', verbose_name='Notice')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'db_table': 'views',
            },
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Notice.Notice', verbose_name='Notice')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'db_table': 'bookmarks',
            },
        ),
    ]
