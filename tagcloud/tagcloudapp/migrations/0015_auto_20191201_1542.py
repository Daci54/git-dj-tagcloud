# Generated by Django 2.2.7 on 2019-12-01 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tagcloudapp', '0014_auto_20191201_0132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='createdby',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='submittedby',
        ),
        migrations.AddField(
            model_name='tag',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tags_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tag',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='TagSubmitHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitted_on', models.DateTimeField(auto_now_add=True)),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tagcloudapp.Tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='tag',
            name='usersubmits',
            field=models.ManyToManyField(related_name='tags_submitted', through='tagcloudapp.TagSubmitHistory', to=settings.AUTH_USER_MODEL),
        ),
    ]