# Generated by Django 5.2.3 on 2025-07-16 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('message', models.TextField()),
                ('sent_on', models.DateField(auto_now_add=True)),
                ('read', models.BooleanField(default=False)),
            ],
        ),
    ]
