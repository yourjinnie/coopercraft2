from django.db import models
from store.models.category import Category
from store.models.collections import Collection
from store.models.offer import Offer


class Product(models.Model):
    product_title = models.CharField(max_length=200)
    product_description=models.TextField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE,default=1)
    product_price=models.DecimalField(max_digits=10,decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    image=models.ImageField(upload_to='images/')
    offer = models.ForeignKey(Offer, null=True, blank=True, on_delete=models.SET_NULL)

    def get_final_price(self):
        if self.offer:
            discount = (self.product_price * self.offer.discount_percentage) / 100
            return self.product_price - discount
        return self.product_price

    def __str__(self):
        return self.product_title

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_product_by_category_id(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.objects.all()

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)