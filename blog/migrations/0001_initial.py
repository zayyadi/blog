# Generated by Django 4.2.7 on 2024-10-24 15:35

import blog.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_summernote.fields
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content', django_summernote.fields.SummernoteTextField()),
                ('image', models.ImageField(default='article/default.jpg', upload_to=blog.models.path_and_rename)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('snippet', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['-publish'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('body', models.TextField()),
                ('publish', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('email', models.EmailField(default='wk@example.com', max_length=254)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='blog.comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.article')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
