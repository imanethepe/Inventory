# Generated by Django 3.2.5 on 2023-11-02 15:00

from django.db import migrations, models


def add_estimated_price_data(apps, schema_editor):
    Item = apps.get_model(
        'goods', 'Item')

    query = Item.objects.all()
    for item in query:
        item.save()


def remove_estimated_price_data(apps, schema_editor):
    Item = apps.get_model(
        'goods', 'Item')

    Item.objects.update(estimated_price=0)


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='Item',
            name='estimated_price',
            field=models.IntegerField(default=0),
            ),
        migrations.AlterField(
            model_name='Item',
            name='estimated_price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
            ),
        migrations.RunPython(
            add_estimated_price_data,
            reverse_code=remove_estimated_price_data
            ),
    ]
