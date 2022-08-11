
from cart.cart import Cart
from .models import *
from cart.forms import CartAddProductForm

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Войти", 'url_name': 'login'},
        {'title': "Регистрация", 'url_name': 'register'}
]


class DataMixin:

    def get_rub_data(self, **kwargs):
        context = kwargs
        rubs = Rub.objects.all()
        context['rubs'] = rubs
        if 'rub_selected' not in context:
            context['rub_selected'] = 0
        context['menu'] = menu
        cart_product_form = CartAddProductForm()
        context['cart_product_form'] = cart_product_form
        return context

