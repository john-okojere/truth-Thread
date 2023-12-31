# Generated by Django 4.1.7 on 2023-12-29 09:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_email_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(error_messages={'unique': 'This email has been used already'}, max_length=254, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(error_messages={'unique': 'This Phone has been used already'}, help_text="Phone number must be entered in the format: '+999999999'.", max_length=16, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+\\d{8,15}$')]),
        ),
    ]
