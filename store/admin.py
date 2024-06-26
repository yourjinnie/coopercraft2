from django.contrib import admin
from .models.product_detail import Product

# Register your models here.
@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['pr_detail','product_description','product_title','product_price','rating','image']