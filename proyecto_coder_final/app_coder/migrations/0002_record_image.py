# Generated by Django 4.2.6 on 2023-10-20 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_coder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
