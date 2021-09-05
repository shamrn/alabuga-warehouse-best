from django.shortcuts import redirect
from .models import Product

def add_product(request, pk):
    """
    Добавляем +10 единиц к товару
    """
    _product = Product.objects.get(pk=pk)
    _product.quantity += 10
    _product.save()
    return redirect('/admin/electronic/product')