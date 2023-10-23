# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 18:00:55 2023

@author: Imanethepe
"""

from django.shortcuts import redirect


def redirect_root(request):
    return redirect('goods_item_list')
