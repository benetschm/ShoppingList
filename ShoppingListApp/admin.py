from django.contrib import admin
from .models import StoreLocation
from .models import HomeLocation
from .models import ShoppingItem

admin.site.register(StoreLocation)
admin.site.register(HomeLocation)
admin.site.register(ShoppingItem)
