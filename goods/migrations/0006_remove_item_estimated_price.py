# Generated by Django 3.2.5 on 2023-11-14 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_auto_20231114_1553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='estimated_price',
        ),
    ]
