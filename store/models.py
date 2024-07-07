from django.db import models
from django.contrib.postgres.fields import ArrayField
import datetime
from PIL import Image


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    pub_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(default="Image" ,upload_to='store/')   
    remained_quantity = models.IntegerField(default=10)
    
    def __str__(self):
        return self.name
    

class Group(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sex = models.CharField(max_length=100,blank=True)
    type1 = models.CharField(max_length=100,blank=True)
    type2 = models.CharField(max_length=100,blank=True)

class Color(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.color

class Style(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    style = models.CharField(max_length=200,blank=True, null=True)

class Description(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description1 = models.TextField(max_length=200,blank=True, null=True)
    description2 = models.TextField(max_length=500,blank=True, null=True)

