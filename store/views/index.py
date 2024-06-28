from django.views import View
from store.models.products import Product
from store.models.category import Category
from store.models.collections import Collection
from django.shortcuts import render,redirect

class Index(View):
    def get(self, request):
        products = Product.get_all_products()
        categories = Category.objects.all()
        collections=Collection.objects.all()
        category_id = request.GET.get('category')

        if category_id:
            products = Product.get_product_by_category_id(category_id)
        else:
            products = Product.get_all_products()
        context = {
            'products': products,
            'categories': categories,
            'collections':collections
        }
        return render(request, 'index.html', context)