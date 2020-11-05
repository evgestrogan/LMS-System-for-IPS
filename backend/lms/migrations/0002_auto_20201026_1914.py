# Generated by Django 2.2 on 2020-10-26 19:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='lms.StudyGroup', verbose_name='Номер учебной группы'),
        ),
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.OneToOneField(limit_choices_to={'user__is_staff': False}, on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL, verbose_name='Информация о пользователе'),
        ),
    ]