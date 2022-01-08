from django.contrib import admin

from sale.models import Category, Sale

# Register your models here.
admin.site.register(Sale)
admin.site.register(Category)