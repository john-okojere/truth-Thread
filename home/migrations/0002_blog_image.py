# Generated by Django 4.1.7 on 2023-12-29 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(null=True, upload_to='Blog/%y/%m/%d'),
        ),
    ]