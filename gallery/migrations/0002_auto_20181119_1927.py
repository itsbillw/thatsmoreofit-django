# Generated by Django 2.1.1 on 2018-11-20 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.ImageField(upload_to='images'),
        ),
    ]
