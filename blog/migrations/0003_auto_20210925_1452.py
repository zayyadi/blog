# Generated by Django 3.2.5 on 2021-09-25 13:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20210924_1602'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.ManyToManyField(related_name='authors', to=settings.AUTH_USER_MODEL),
        ),
    ]