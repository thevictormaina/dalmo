# Generated by Django 3.2.8 on 2021-10-14 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_entry_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='rating',
            field=models.PositiveIntegerField(choices=[(5, 'really good'), (4, 'good'), (3, 'neutral'), (2, 'bad'), (1, 'really bad')], default=1),
        ),
    ]
