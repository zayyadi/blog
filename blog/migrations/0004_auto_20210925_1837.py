# Generated by Django 3.2.5 on 2021-09-25 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210925_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default='zayyad', max_length=255),
        ),
    ]
