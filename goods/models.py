from django.db import models
from django.urls import reverse

# Create your models here.


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


class Item(models.Model):
    name = models.CharField(
        max_length=31, db_index=True)
    slug = models.SlugField(
         max_length=31,
         unique=True,
         help_text='A label for URL conﬁg.')
    description = models.TextField()
    quantity = models.CharField(
        max_length=31, db_index=True)
    # estimated_price = models.CharField(
    #     max_length=31, db_index=True)
    entry_date = models.DateField(
        'date of entry')
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        ordering = ['name']
        get_latest_by = 'entry_date'

    def __str__(self):
        return self.name
