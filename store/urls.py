"""
URL configuration for GREATKART project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.store,name="store"),
    path('catergory/<slug:catergory_slug>/',views.store,name="products_by_catergory"),
    path('catergory/<slug:catergory_slug>/<slug:product_slug>/',views.product_detail,name="product_detail"),
    path('search/',views.search,name="search"),
]
