# Generated by Django 3.0.5 on 2020-05-11 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citizen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='compliant',
            name='district',
            field=models.CharField(default='District', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compliant',
            name='place',
            field=models.CharField(default='place', max_length=50),
            preserve_default=False,
        ),
    ]
