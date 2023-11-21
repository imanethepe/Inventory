# Generated by Django 3.2.5 on 2023-11-14 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0006_remove_item_estimated_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='estimated_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]