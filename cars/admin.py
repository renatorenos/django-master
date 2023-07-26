from django.contrib import admin
from cars.models import Car, Brand

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model', 'brand')

class BrandAdmin(admin.ModelAdmin):
    list_display = ('model',)
    search_fields = ('model',)

admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)