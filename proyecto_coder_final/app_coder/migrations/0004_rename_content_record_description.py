# Generated by Django 4.2.6 on 2023-10-20 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_coder', '0003_record_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='content',
            new_name='description',
        ),
    ]