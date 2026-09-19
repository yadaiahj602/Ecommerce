from django.db import models
from greatkar.models import Catergory
from django.urls import reverse

# Create your models here.
class Product(models.Model):
  product_name = models.CharField(max_length=120,unique=True)
  slug = models.SlugField(max_length=200,unique=True)
  desc = models.TextField(max_length=500,blank=True)
  price = models.IntegerField()
  images = models.ImageField(upload_to='photos/products')
  stock = models.IntegerField()
  is_available = models.BooleanField(default=True)
  catergory = models.ForeignKey(Catergory,on_delete=models.CASCADE)
  created_date = models.DateTimeField(auto_now_add=True)
  modified_date = models.DateTimeField(auto_now=True)
  
  def get_url(self):
    return reverse('product_detail',args=[self.catergory.slug,self.slug])
    
  
  def __str__(self):
    return self.product_name
  
  