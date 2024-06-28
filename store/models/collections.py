from django.db import models

class Collection(models.Model):
    collection=models.CharField(max_length=100)
    collection_image=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.collection