# Generated by Django 2.2.5 on 2019-10-17 20:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Notice', '0004_bookmark_view'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='View',
            new_name='NoticeView',
        ),
        migrations.CreateModel(
            name='AdministrationNotice',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('Notice.notice',),
        ),
        migrations.CreateModel(
            name='SocietyNotice',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('Notice.notice',),
        ),
        migrations.CreateModel(
            name='Interested',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Notice.Notice', verbose_name='Notice')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'db_table': 'interested',
            },
        ),
    ]
