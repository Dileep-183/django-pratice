# Generated by Django 2.2 on 2021-09-08 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0007_auto_20210908_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='is_staff',
            field=models.BooleanField(),
        ),
    ]
