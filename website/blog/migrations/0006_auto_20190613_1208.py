# Generated by Django 2.2.2 on 2019-06-13 06:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_functionsavailable_authorname'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Functionsavailable',
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
