# Generated by Django 2.1.7 on 2019-03-17 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': ' category', 'verbose_name_plural': 'categories'},
        ),
    ]
