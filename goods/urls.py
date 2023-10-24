# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 14:40:00 2023

@author: Nathalie
"""

from django.urls import path, re_path
from .views import (
    TagList, ItemList,
    TagDetail, ItemDetail)

urlpatterns = [
    path(r'tag/',
         TagList.as_view(),
         name='goods_tag_list'),
    path(r'item/',
         ItemList.as_view(),
         name='goods_item_list'),
    re_path(r'tag/(?P<slug>[\w\-]+)/$',
            TagDetail.as_view(),
            name='goods_tag_detail'),
    re_path(r'item/(?P<slug>[\w\-]+)/$',
            ItemDetail.as_view(),
            name='goods_item_detail'),

]
