# Generated by Django 4.2.7 on 2023-11-26 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productweb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.CharField(default='No description', max_length=255),
        ),
    ]