# Generated by Django 2.2.7 on 2019-11-16 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tagcloudapp', '0005_auto_20191116_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='tag',
            field=models.ManyToManyField(null=True, to='tagcloudapp.Tag'),
        ),
    ]
