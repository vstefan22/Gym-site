# Generated by Django 4.1.2 on 2022-10-22 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0002_membershipplan_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='membershipplan',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
