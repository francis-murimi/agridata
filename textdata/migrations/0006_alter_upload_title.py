# Generated by Django 4.0.3 on 2022-05-24 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textdata', '0005_alter_upload_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
