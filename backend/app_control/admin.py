from django.contrib import admin
from .models import Inventory, InventoryGroup, Shop

admin.site.register((InventoryGroup, Inventory, Shop))
