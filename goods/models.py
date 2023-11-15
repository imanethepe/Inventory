from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(
        max_length=31, unique=True)
    slug = models.SlugField(
        max_length=31,
        unique=True,
        help_text='A label for URL conﬁg.')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'goods_tag_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse(
            'goods_tag_update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse(
            'goods_tag_delete', kwargs={'slug': self.slug})


class Item(models.Model):
    name = models.CharField(
        max_length=31, db_index=True)
    slug = models.SlugField(
         max_length=31,
         unique=True,
         help_text='A label for URL conﬁg.')
    description = models.TextField()
    quantity = models.IntegerField(default=0)
    estimated_price = models.DecimalField(
        decimal_places=2, max_digits=5, default=0.000)
    total_item_estimated_price = models.DecimalField(
          decimal_places=2, max_digits=5, default=0.000)
    total_inventory_value = models.DecimalField(
          decimal_places=2, max_digits=5, default=0.000)
    entry_date = models.DateField(
        'date of entry')
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        ordering = ['name']
        get_latest_by = 'entry_date'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'goods_item_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse(
            'goods_item_update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse(
            'goods_item_delete', kwargs={'slug': self.slug})
