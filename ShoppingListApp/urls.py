from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.shoppingitem_list, name='shoppingitem_list'),
]
