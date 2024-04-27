from django.contrib import admin
from .models import Category, Cleaners, Order, OrderItem


admin.site.register(Category)
admin.site.register(Cleaners)
admin.site.register(Order)
admin.site.register(OrderItem)