from django.contrib import admin
from .models import Delivery

class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'delivery_address', 'delivery_date', 'order_id', 'delivery_cost')

admin.site.register(Delivery, DeliveryAdmin)

# Register your models here.
