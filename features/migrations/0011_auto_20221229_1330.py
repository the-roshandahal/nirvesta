# Generated by Django 3.2 on 2022-12-29 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0010_boardmember'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardmember',
            name='facebook_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='boardmember',
            name='instagram_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='boardmember',
            name='linkedin_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='boardmember',
            name='twitter_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='facebook_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='instagram_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='linkedin_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='twitter_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]