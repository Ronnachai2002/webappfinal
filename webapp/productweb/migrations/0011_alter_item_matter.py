# Generated by Django 4.2.7 on 2023-11-26 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productweb', '0010_item_matter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='matter',
            field=models.CharField(default='No description', max_length=50),
        ),
    ]