# Generated by Django 3.2 on 2023-02-01 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0046_rename_citi_back_loan_others'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loan',
            old_name='citi_front',
            new_name='citizenship',
        ),
    ]
