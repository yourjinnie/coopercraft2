from django.views import View
from store.models.product_detail import Product
from django.shortcuts import render,redirect

class ProductDetail(View):
    def get(self,request):
        products=Product.objects.all()
        return render(request,'product-detail.html', {products})
