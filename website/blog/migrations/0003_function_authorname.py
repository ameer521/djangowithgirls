# Generated by Django 2.2.2 on 2019-06-13 06:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_function'),
    ]

    operations = [
        migrations.AddField(
            model_name='function',
            name='authorname',
            field=models.ForeignKey(default='ameer', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
