# Generated by Django 4.0.2 on 2022-02-04 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='server',
            name='access',
        ),
    ]
