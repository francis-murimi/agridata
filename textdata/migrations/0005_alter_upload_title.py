# Generated by Django 4.0.3 on 2022-05-24 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textdata', '0004_alter_upload_textfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='title',
            field=models.CharField(default='Agriculture', max_length=30),
        ),
    ]