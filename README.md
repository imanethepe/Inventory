# Inventory for custom
# Part 1: Setting of two basic pages, the list of items and the list of tags 
          linked to pages detailing of each item and tag.
          The main fields of the model Item are name, description, quantity,
          entry_date, slug.
          Assuming the data base filled with information, we would like to add
          another field 'estimated_price' without damaging the existing 
          database. The option is to set the new field in the directory 
          migrations.
# Part 2: Adding of the field total_item_estimated_price for each item depending 
          on its quantity.
          In views.py:
          Use of queryset expressions to update the field total_item_estimated_price
          and to estimate the total_inventory_value by summing the column of the field
          total_item_estimated_price.
# Part 3: Adding of the choice of currencies (EURO, USD, CAD).
          Adding of the update of the currency of the whole items and the total_inventory_value
          if one currency is changed.

