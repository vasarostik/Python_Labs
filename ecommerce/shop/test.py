from django.test import TestCase
from orders.models import Order, OrderItem
from shop.models import Category
from shop.models import Product
from cart.cart import Cart
from . import views
from django.test import Client
from cart.views import cart_detail
from django.urls import reverse
from django.conf.urls import url
from cart.cart import Cart
from django.http.request import HttpRequest
from django.conf import settings
from importlib import import_module

class Category_test(TestCase):

    @classmethod
    def setUpClass(self):
        Category.objects.create(name="Bike",slug="bike")
        Order.objects.create(first_name="Hornet")
        Product.objects.create(name="tess", category=Category.objects.get(name="Bike"), slug="tess", price=100,
                               stock=10)
        # orderitem
        OrderItem.objects.create(order=Order.objects.get(first_name="Hornet"), product=Product.objects.get(name="tess"),
                                 price=10, quantity=3)
        # creating instance of a client.
        self.client = Client()

    def test_getLogin(self):
        category = Category.objects.get(name="Bike")
        order = Order.objects.get(first_name="Hornet")
        prod = Product.objects.get(name="tess")
        orderitem = OrderItem.objects.get(product=Product.objects.get(name="tess"))

        #product
        self.assertEqual(prod.__str__(), "tess")
        self.assertEqual(prod.get_absolute_url(), "/1/tess/")

        #orderitem
        self.assertEqual(orderitem.get_cost(), 30)
        self.assertEqual(orderitem.__int__(), 3)
        self.assertEqual(orderitem.__str__(), "1")

        #category
        self.assertEqual(category.__str__(), "Bike")
        self.assertEqual(category.get_absolute_url(), "/bike/")
        #order
        self.assertEqual(order.str(), "Hornet")
        self.assertEqual(order.__str__(), "Order 1")
        self.assertEqual(order.get_total_cost(), 30)

        # cart
        response = self.client.post(reverse('cart:cart_detail'))
        response1 = self.client.post(reverse('cart:cart_add', args=[prod.id]))
        response2 = self.client.post(reverse('cart:cart_remove', args=[prod.id]))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response1.status_code, 302)
        self.assertEqual(response2.status_code, 302)

        # orders
        response3 = self.client.post(reverse('orders:order_create'))

        self.assertEqual(response3.status_code, 200)

        #shop
        response4 = self.client.post(reverse('shop:product_list'))
        response5 = self.client.post(reverse('shop:product_detail', args=[prod.id, prod.slug]))

        self.assertEqual(response4.status_code, 200)
        self.assertEqual(response5.status_code, 200)

        request = HttpRequest()
        engine = import_module(settings.SESSION_ENGINE)
        session_key = None
        request.session = engine.SessionStore(session_key)
        cart = Cart(request)
        self.assertEqual(cart.__len__(),0)
        self.assertEqual(cart.get_total_price(), 0)

    @classmethod
    def tearDownClass(cls):
        pass
