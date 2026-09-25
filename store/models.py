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

class VariationManager(models.Manager):
  def colors(self):
    return super(VariationManager,self).filter(variation_catergory='color', is_active=True)
  
  def sizes(self):
    return super(VariationManager,self).filter(variation_catergory='size', is_active=True)
  
variation_catergory_choice = (
  ('color','color'),
  ('size','size'),
)

class Variation(models.Model):
  product = models.ForeignKey(Product,on_delete=models.CASCADE)
  variation_catergory = models.CharField(max_length=100, choices=variation_catergory_choice)
  variation_value = models.CharField(max_length=100)
  is_active = models.BooleanField(default=True)
  created_date = models.DateTimeField(auto_now=True)
  
  objects = VariationManager()
  
  def __str__(self):
    return self.variation_value