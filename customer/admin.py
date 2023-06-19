from django.contrib import admin
from.models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display=("customer_id","first_name","second_name","email")
admin.site.register(Customer,CustomerAdmin)

# Register your models here.
