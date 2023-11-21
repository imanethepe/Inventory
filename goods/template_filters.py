# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 15:59:14 2023

@author: Imanethepe
"""

from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
