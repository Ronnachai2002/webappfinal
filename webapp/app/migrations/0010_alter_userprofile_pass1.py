# Generated by Django 4.2.7 on 2023-12-20 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_userprofile_pass1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='pass1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
