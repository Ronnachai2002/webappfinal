# Generated by Django 4.2.7 on 2023-11-26 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productweb', '0007_alter_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='productweb\\media\\product_images'),
        ),
    ]
