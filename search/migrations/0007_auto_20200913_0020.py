# Generated by Django 3.0.5 on 2020-09-12 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0006_auto_20200913_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(null=True, upload_to='search/static/search/images/'),
        ),
    ]
