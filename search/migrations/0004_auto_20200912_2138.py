# Generated by Django 3.0.5 on 2020-09-12 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_auto_20200912_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(null=True, upload_to='./'),
        ),
    ]
