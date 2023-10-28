from django.shortcuts import (
    render, get_object_or_404)
from django.views.generic import View
from .models import Tag, Item
from .forms import TagForm, ItemForm
from .utils import ObjectCreateMixin


class TagList(View):
    """Get request of the list of tags"""

    def get(self, request):
        return render(
            request,
            'goods/tag_list.html',
            {'tag_list': Tag.objects.all()})


class ItemList(View):
    """Get request of the list of items"""

    def get(self, request):
        return render(
            request,
            'goods/item_list.html',
            {'item_list': Item.objects.all()})


class TagDetail(View):
    """Get and post requests of a tag"""

    def get(self, request, slug):
        tag = get_object_or_404(
            Tag, slug=slug)
        return render(
            request,
            'goods/tag_detail.html',
            {'tag': tag})


class ItemDetail(View):
    """Get and post requests of a item"""

    def get(self, request, slug):
        item = get_object_or_404(
            Item, slug=slug)
        return render(
            request,
            'goods/item_detail.html',
            {'item': item})


class TagCreate(ObjectCreateMixin, View):
    """Post request of a new tag"""

    form_class = TagForm
    template_name = 'goods/tag_form.html'


class ItemCreate(ObjectCreateMixin, View):
    """Post request of a new item"""

    form_class = ItemForm
    template_name = 'goods/item_form.html'