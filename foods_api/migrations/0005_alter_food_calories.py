# Generated by Django 3.2.9 on 2021-11-21 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods_api', '0004_food_linked_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='calories',
            field=models.FloatField(),
        ),
    ]
