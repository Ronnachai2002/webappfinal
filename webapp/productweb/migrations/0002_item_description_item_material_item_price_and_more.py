# Generated by Django 4.2.7 on 2023-12-20 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productweb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='No description', max_length=255),
        ),
        migrations.AddField(
            model_name='item',
            name='material',
            field=models.CharField(default='No description', max_length=50),
        ),
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='size',
            field=models.CharField(max_length=500),
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='productweb.item')),
            ],
        ),
    ]
