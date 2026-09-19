from django.db import models
from django.urls import reverse

# Create your models here.
class Catergory(models.Model):
  catergory_name = models.CharField(max_length=50,unique=True)
  slug = models.SlugField(max_length=100,unique=True)
  des = models.TextField(max_length=225,blank=True)
  cat_img = models.ImageField(upload_to = "photos/categories",blank=True)
  
  class Meta:
    verbose_name = 'catergory'
    verbose_name_plural = 'categories'
  
  
  def get_url(self):
    return reverse('products_by_catergory',args=[self.slug])
  
  def __str__(self):
    return self.catergory_name