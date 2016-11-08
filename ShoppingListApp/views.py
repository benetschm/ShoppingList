from django.shortcuts import render

# Create your views here.

def shoppingitem_list(request):
    return render(request, 'ShoppingListApp/shoppingitem_list.html', {})
