# Generated by Django 2.1.7 on 2019-03-17 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0003_meals_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meals',
            options={'verbose_name': 'meal', 'verbose_name_plural': 'meals'},
        ),
    ]
