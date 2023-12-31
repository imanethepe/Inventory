# Generated by Django 3.2.5 on 2023-11-13 13:40

from django.db import migrations, models


def add_total_inventory_value_data(apps, schema_editor):
    Item = apps.get_model(
        'goods', 'Item')

    query = Item.objects.all()
    for item in query:
        item.save()


def remove_total_inventory_value_data(apps, schema_editor):
    Item = apps.get_model(
        'goods', 'Item')

    Item.objects.update(total_inventory_value=0.000)


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_total_item_estimated_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='Item',
            name='total_inventory_value',
            field=models.DecimalField(
                decimal_places=2, max_digits=5, default=0.000),
            ),
        migrations.RunPython(
            add_total_inventory_value_data,
            reverse_code=remove_total_inventory_value_data
            ),
    ]
