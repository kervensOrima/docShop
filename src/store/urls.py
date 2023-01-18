from django.urls import path

from store.views import index, product_detail, add_to_cart, cart, cart_delete

app_name = "store"

urlpatterns = [
    path('', index, name="index"),
    path('cart/', cart, name="cart"),
    path('cart/delete', cart_delete, name="cart_delete"),
    path('<str:slug>/product-detail/', product_detail, name="product_detail"),
    path('<str:slug>/product-detail/add-to-cart/', add_to_cart, name="add_to_cart")
]
