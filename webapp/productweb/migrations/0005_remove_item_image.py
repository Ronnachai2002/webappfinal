# Generated by Django 4.2.7 on 2023-11-26 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productweb', '0004_alter_item_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='image',
        ),
    ]