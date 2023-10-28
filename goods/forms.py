# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 14:39:44 2023

@author: Imanethepe
"""

from django import forms
from django.core.exceptions import ValidationError
from .models import Tag, Item


class SlugCleanMixin:
    """Mixin class for slug cleaning method."""

    def clean_slug(self):
        new_slug = (
            self.cleaned_data['slug'].lower())
        if new_slug == 'create':
            raise ValidationError(
                'Slug may not be "create".')
        return new_slug


class TagForm(
        SlugCleanMixin, forms.ModelForm):
    """Attributes similar to model"""

    class Meta:
        model = Tag
        ﬁelds = '__all__'

    def clean_name(self):
        return self.cleaned_data['name'].lower()


class ItemForm(
        SlugCleanMixin, forms.ModelForm):
    """Attributes similar to model"""

    class Meta:
        model = Item
        ﬁelds = '__all__'

    def clean_name(self):
        return self.cleaned_data['name'].lower()
