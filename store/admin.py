from django.contrib import admin
from .models.products import Product
from .models.category import Category
from .models.offer import Offer
from .models.collections import Collection

# Register your models here.
@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['product_title','category','product_description','product_price','rating','offer','image']

admin.site.register(Category)
admin.site.register(Offer)
admin.site.register(Collection)

