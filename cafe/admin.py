# cafe/admin.py
from django.contrib import admin
from .models import Category,Item,Order

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Order)
# Register your models here.
