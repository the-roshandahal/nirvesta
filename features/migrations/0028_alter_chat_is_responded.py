# Generated by Django 3.2 on 2023-01-03 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0027_chat_is_responded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='is_responded',
            field=models.BooleanField(),
        ),
    ]
