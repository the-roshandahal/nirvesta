# Generated by Django 3.2 on 2023-02-01 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0045_auto_20230131_1105'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loan',
            old_name='citi_back',
            new_name='others',
        ),
    ]
