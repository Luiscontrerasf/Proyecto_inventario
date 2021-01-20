from django.contrib import admin
from .models import producto, movimiento, stock

# Register your models here.


admin.site.register(producto)
admin.site.register(movimiento)
admin.site.register(stock)
