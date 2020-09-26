# Generated by Django 3.1 on 2020-08-28 23:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.URLField()),
                ('twitter_acc', models.URLField(blank=True, max_length=300, null=True)),
                ('facebook_acc', models.URLField(blank=True, max_length=300, null=True)),
                ('instagram_acc', models.URLField(blank=True, max_length=300, null=True)),
                ('user_bio', models.TextField(blank=True, max_length=500, null=True)),
                ('newsletter_sub', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE,
                                              to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
