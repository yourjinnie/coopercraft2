from django.contrib import admin
from .models.products import Product
from .models.category import Category

# Register your models here.
@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['product_title','category','product_description','product_price','rating','image']

admin.site.register(Category)

