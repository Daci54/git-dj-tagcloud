# Generated by Django 2.2.7 on 2019-11-30 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tagcloudapp', '0010_auto_20191130_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, related_name='subjects', to='tagcloudapp.Tag'),
        ),
    ]