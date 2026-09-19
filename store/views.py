from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Product
from greatkar.models import Catergory


# Create your views here.
def store(request,catergory_slug=None):
  categories = None
  products = None
  
  if catergory_slug != None:
    categories = get_object_or_404(Catergory,slug=catergory_slug)
    products = Product.objects.filter(catergory = categories, is_available=True)
    tot = products.count()
  else:
    products = Product.objects.filter(is_available=True)
    tot = products.count()
  context = {
      'products':products,
      'totals':tot,
    }
  return render(request,'store.html',context)

def product_detail(request,catergory_slug,product_slug):
  try:
    single_pro = Product.objects.get(catergory__slug=catergory_slug,slug=product_slug)
  except Exception as e:
    raise e
  context={
    'single_pro':single_pro,
  }
  return render(request,'product-detail.html',context)