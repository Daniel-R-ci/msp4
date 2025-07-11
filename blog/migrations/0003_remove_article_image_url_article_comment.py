# Generated by Django 5.2.3 on 2025-07-07 07:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_article_draft_article_published'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='image_url',
        ),
        migrations.CreateModel(
            name='Article_Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('visible', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_commenter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
