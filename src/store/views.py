import logging

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.urls import reverse

from store.models import Product, Cart, Order


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    products = Product.objects.all()
    return render(request=request, template_name="store/index.html", context={
        "title": "La boutique OK Fresh up",
        'products': products
    })


def product_detail(request, slug: str) -> HttpResponse:
    product = None
    try:
        product = Product.objects.get(slug=slug)
    except Exception as e:
        logging.error(e)
        return HttpResponse("Product not found!")
    return render(request=request, template_name="store/product_detail.html", context={
        'product': product,
        'title': product.name
    })


def add_to_cart(request: HttpRequest, slug: str) -> str:
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    c, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user,
                                                 ordered=False,
                                                 product=product)
    if created:
        c.orders.add(order)
        c.save()
    else:
        order.quantity += 1
        order.save()
    return redirect(reverse('store:product_detail', kwargs={'slug': slug}))


def cart(request: HttpRequest) -> HttpResponse:
    template = loader.get_template("store/cart.html")
    context = {}
    try:
        c = Cart.objects.get(user=request.user)
        context['cart'] = c
        context['title'] = f"{c.user.username} Liste des articles au panier"
    except Exception as e:
        logging.error(e)
        return HttpResponse('Cart not found')

    return HttpResponse(template.render(context, request))


def cart_delete(request: HttpRequest) -> HttpResponse:
    if c := request.user.cart:
        # c.orders.all().delete()
        c.delete()
    return redirect('store:index')

# def _add_to_cart(request: HttpRequest, slug: str) -> HttpResponse:
#     user = request.user
#     product = None
#     cart = None
#     order = None
#     try:
#         product = Product.objects.get(slug=slug)
#         if product:
#             cart = Cart.objects.get(user=user)
#             if cart:
#                 order = Order.objects.get(user__email=user.email, product__id=product.id)
#                 if order:
#                     cart.orders.add(order)
#                     cart.save()
#                 else:
#                     order.quantity += 1
#                     order.save()
#                 return redirect(reverse('store:product_detail', kwargs={'slug': slug}))
#
#     except Exception as e:
#         logging.error(e)
#         return HttpResponse('<h1>Object not found</h1>')
