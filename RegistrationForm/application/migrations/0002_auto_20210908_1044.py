# Generated by Django 2.2 on 2021-09-08 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='gender',
            field=models.BooleanField(choices=[('M', 'Male'), ('F', 'Female')]),
        ),
    ]
