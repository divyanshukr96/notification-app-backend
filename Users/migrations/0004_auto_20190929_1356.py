# Generated by Django 2.2.5 on 2019-09-29 08:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_auto_20190929_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='department',
            field=models.ForeignKey(limit_choices_to={'is_admin': False, 'user_type': 'DEPARTMENT'}, on_delete=django.db.models.deletion.CASCADE, related_name='faculty_department', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.ForeignKey(limit_choices_to={'is_admin': False, 'user_type': 'DEPARTMENT'}, on_delete=django.db.models.deletion.CASCADE, related_name='student_department', to=settings.AUTH_USER_MODEL),
        ),
    ]
