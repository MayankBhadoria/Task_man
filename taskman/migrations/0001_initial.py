# Generated by Django 4.0.2 on 2023-08-16 09:35

import datetime
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
            name='todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('completed', 'completed')], max_length=20)),
                ('date', models.DateField(default=datetime.date.today)),
                ('priority', models.CharField(choices=[('low', 'low'), ('medium', 'medium'), ('high', 'high')], max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
