from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Product
from greatkar.models import Catergory
from cart.models import CartItem
from cart.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

# Create your views here.
def store(request,catergory_slug=None):
  categories = None
  products = None
  
  if catergory_slug != None:
    categories = get_object_or_404(Catergory,slug=catergory_slug)
    products = Product.objects.filter(catergory = categories, is_available=True)
    paginator = Paginator(products, 3)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    tot = products.count()
  else:
    products = Product.objects.filter(is_available=True).order_by('id')
    paginator = Paginator(products, 3)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    tot = products.count()
  context = {
      'products':paged_products,
      'totals':tot,
    }
  return render(request,'store.html',context)

def product_detail(request,catergory_slug,product_slug):
  try:
    single_pro = Product.objects.get(catergory__slug=catergory_slug,slug=product_slug)
    in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request),product=single_pro).exists()
  except Exception as e:
    raise e
  return render(request,'product-detail.html',{'single_pro':single_pro,'in_cart':in_cart})

def search(request):
  if 'keyword' in request.GET:
    keyword = request.GET['keyword']
    if keyword:
      products = Product.objects.order_by('-created_date').filter(Q(desc__icontains=keyword) | Q(product_name__icontains=keyword))
      tot = products.count()
  context = {
    'products':products,
    'totals':tot,
  }
  return render(request,'store.html',context)

