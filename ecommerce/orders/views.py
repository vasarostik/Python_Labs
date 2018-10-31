from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from shop.models import Product
from django.shortcuts import render, redirect, get_object_or_404
from cart.forms import CartAddProductForm


def order_create(request):

    cart = Cart(request)
    print(type(cart))
    cart1 = cart
    mass = []
    for item in cart1:
        product = get_object_or_404(Product, name=item['product'])
        print(product.id)
        if product.stock == 0:
            mass.append(product.name)
            # cart1.remove_kolizion(product)
            # break
    print(mass)
    # delete all colizions
    for name in mass:
        product = get_object_or_404(Product, name=name)
        cart1.remove_kolizion(product)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        cart = Cart(request)
        if form.is_valid():
            order = form.save()
            for item in cart:
                product = get_object_or_404(Product, name=item['product'])

                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
                # update to reduce amount in stock-------------------------------------------
                to_edit = Product.objects.get(name=item['product'])

                to_edit.stock = product.stock - item['quantity']
                # available = false
                if to_edit.stock == 0:
                    to_edit.available = False
                to_edit.save()
                # ------------------------end----------------------------------------------

            cart.clear()
            return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()

    return render(request, 'orders/order/create.html', {'form': form})
