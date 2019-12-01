# Generated by Django 2.2.7 on 2019-11-30 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tagcloudapp', '0012_auto_20191130_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='tag',
        ),
        migrations.AddField(
            model_name='tag',
            name='subjects',
            field=models.ManyToManyField(blank=True, related_name='tags', to='tagcloudapp.Subject'),
        ),
    ]
