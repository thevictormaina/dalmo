# Generated by Django 3.2.8 on 2021-10-13 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20211013_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date_added',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='moment',
            name='date_added',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
