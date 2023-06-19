from django.contrib import admin
from.models import Category
class Category_admin(admin.ModelAdmin):
    list_display=["name"]
admin.site.register(Category,Category_admin)

# Register your models here.
