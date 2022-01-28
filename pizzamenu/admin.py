from django.contrib import admin
from . models import Pizzamenu

# Register your models here.

class PizzamenuAdmin(admin.ModelAdmin):
 list_display = ('name', 'price')

admin.site.register(Pizzamenu, PizzamenuAdmin)