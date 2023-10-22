# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 14:40:00 2023

@author: Nathalie
"""

from django.urls import path
from .views import TagList, ItemList

urlpatterns = [
    path(r'tag/',
         TagList.as_view(),
         name='goods_tag_list'),
    path(r'item/',
         ItemList.as_view(),
         name='goods_item_list'),
]
