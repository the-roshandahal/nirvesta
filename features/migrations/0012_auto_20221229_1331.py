# Generated by Django 3.2 on 2022-12-29 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0011_auto_20221229_1330'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boardmember',
            old_name='facebook_url',
            new_name='facebook',
        ),
        migrations.RenameField(
            model_name='boardmember',
            old_name='instagram_url',
            new_name='instagram',
        ),
        migrations.RenameField(
            model_name='boardmember',
            old_name='linkedin_url',
            new_name='linkedin',
        ),
        migrations.RenameField(
            model_name='boardmember',
            old_name='twitter_url',
            new_name='twitter',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='facebook_url',
            new_name='facebook',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='instagram_url',
            new_name='instagram',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='linkedin_url',
            new_name='linkedin',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='twitter_url',
            new_name='twitter',
        ),
    ]