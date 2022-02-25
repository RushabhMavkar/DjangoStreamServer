# Generated by Django 4.0.2 on 2022-02-18 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0007_alter_userbookmark_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='code',
            field=models.CharField(max_length=256, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='server',
            name='admin',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
