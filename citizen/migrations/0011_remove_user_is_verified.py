# Generated by Django 3.0.5 on 2020-05-13 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('citizen', '0010_auto_20200513_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_verified',
        ),
    ]
