from django.contrib import admin
from .models.country import Country

# Register your models here.
class AdminCountry(admin.ModelAdmin):
    list_display=['name', 'code', 'capital', 'population','id']

admin.site.register(Country, AdminCountry)