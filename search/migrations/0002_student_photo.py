# Generated by Django 3.0.5 on 2020-09-12 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='photo',
            field=models.CharField(max_length=100, null=True),
        ),
    ]