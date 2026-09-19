from django.contrib import admin
from .models import Catergory

# Register your models here.
class CatergoryAd(admin.ModelAdmin):
  prepopulated_fields = {'slug':('catergory_name',)}
  list_display = ('catergory_name','slug')

admin.site.register(Catergory,CatergoryAd)