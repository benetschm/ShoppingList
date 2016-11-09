from django.shortcuts import render
from .models import ShoppingItem

# Create your views here.

def shoppingitem_list(request):
    shoppingitems = ShoppingItem.objects.all()
    return render(request, 'ShoppingListApp/shoppingitem_list.html', {'shoppingitems': shoppingitems})
