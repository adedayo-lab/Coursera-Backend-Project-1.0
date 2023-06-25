# Generated by Django 4.1.3 on 2023-06-21 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_menu_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='description',
        ),
        migrations.AddField(
            model_name='menu',
            name='menu_item_description',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
