from django.db import models


class Product(models.Model):
    pr_detail=models.CharField(max_length=50)
    product_description=models.TextField(max_length=200)
    product_title=models.CharField(max_length=200)
    product_price=models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    image=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.product

    @staticmethod
    def get_all_products():
        return Product.objects.all()