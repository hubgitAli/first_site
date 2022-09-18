# Generated by Django 4.1 on 2022-08-14 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='view_personal',
            name='name',
        ),
        migrations.AddField(
            model_name='view_personal',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
