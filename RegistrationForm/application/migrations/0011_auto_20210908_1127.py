# Generated by Django 2.2 on 2021-09-08 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0010_auto_20210908_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='Address',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registration',
            name='pincode',
            field=models.CharField(default=0, max_length=6),
            preserve_default=False,
        ),
    ]