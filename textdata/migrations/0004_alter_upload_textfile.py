# Generated by Django 4.0.3 on 2022-05-17 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textdata', '0003_upload_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='textfile',
            field=models.FileField(upload_to='documents'),
        ),
    ]