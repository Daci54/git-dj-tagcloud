# Generated by Django 2.2.7 on 2019-12-01 00:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tagcloudapp', '0013_auto_20191201_0059'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='createdby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tag',
            name='submittedby',
            field=models.ManyToManyField(blank=True, related_name='tags', to=settings.AUTH_USER_MODEL),
        ),
    ]
