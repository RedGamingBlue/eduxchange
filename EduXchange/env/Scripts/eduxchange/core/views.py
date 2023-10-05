from django.shortcuts import render, get_object_or_404


from .models import Item



def detail (requesr, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'item/detail.html', {
        'item': item
    })
