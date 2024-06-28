from django.db import models

class Offer(models.Model):
    offer = models.CharField(max_length=255)
    description = models.TextField()
    discount_percentage = models.FloatField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.offer