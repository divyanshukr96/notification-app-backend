# Generated by Django 2.2.5 on 2019-09-25 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Files', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='object_id',
            field=models.UUIDField(),
        ),
    ]
