from django.shortcuts import (
    render, get_object_or_404)
from django.views.generic import View
from django.urls import reverse_lazy
from .models import Tag, Item
from .forms import TagForm, ItemForm
from .utils import (
    ObjectCreateMixin, ObjectUpdateMixin,
    ObjectDeleteMixin)


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


class TagUpdate(ObjectUpdateMixin, View):
    """Post request to update a tag"""

    form_class = TagForm
    model = Tag
    template_name = 'goods/tag_form_update.html'


class ItemUpdate(ObjectUpdateMixin, View):
    """Post request to update an item"""

    form_class = ItemForm
    model = Item
    template_name = 'goods/item_form_update.html'


class TagDelete(ObjectDeleteMixin, View):
    """Post request to delete a tag"""

    model = Tag
    success_url = reverse_lazy(
        'goods_tag_list')
    template_name = 'goods/tag_form_delete.html'


class ItemDelete(ObjectDeleteMixin, View):
    """Post request to delete an item"""

    model = Item
    success_url = reverse_lazy(
        'goods_item_list')
    template_name = 'goods/item_form_delete.html'
