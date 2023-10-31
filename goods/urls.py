# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 14:40:00 2023

@author: Nathalie
"""

from django.urls import path, re_path
from .views import (
    TagList, ItemList,
    TagDetail, ItemDetail,
    TagCreate, ItemCreate,
    TagUpdate, ItemUpdate,
    TagDelete, ItemDelete)

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
    path(r'tag/create',
         TagCreate.as_view(),
         name='goods_tag_create'),
    path(r'item/create',
         ItemCreate.as_view(),
         name='goods_item_create'),
    re_path(r'tag/update/(?P<slug>[\w\-]+)/$',
            TagUpdate.as_view(),
            name='goods_tag_update'),
    re_path(r'item/update/(?P<slug>[\w\-]+)/$',
            ItemUpdate.as_view(),
            name='goods_item_update'),
    re_path(r'tag/delete/(?P<slug>[\w\-]+)/$',
            TagDelete.as_view(),
            name='goods_tag_delete'),
    re_path(r'item/delete/(?P<slug>[\w\-]+)/$',
            ItemDelete.as_view(),
            name='goods_item_delete'),
]
