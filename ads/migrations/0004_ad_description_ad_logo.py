# Generated by Django 5.0.4 on 2024-06-03 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_consumer_ad'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ad',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='logos/'),
        ),
    ]