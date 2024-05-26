from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    style = models.PositiveSmallIntegerField(null=True, blank=True)
    price = models.IntegerField()
    description = models.TextField()
    image = models.FileField(default="Image" ,upload_to='static/images/')
    remained_quantity = models.IntegerField(default=10)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

