# Generated by Django 4.2.7 on 2023-12-18 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productweb', '0014_item_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='size',
            field=models.CharField(max_length=500),
        ),
    ]