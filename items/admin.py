from django.contrib import admin

from .models import Item
from .models import Category

admin.site.register(Item)
admin.site.register(Category)
# Register your models here.
