from django.contrib import admin
from .models import Cloth


# Register your models here.
@admin.register(Cloth)
class ClothAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "size",
        "color",
        "price",
        "stock",
        "created",
        "updated",
    )
    search_fields = ("name", "category")
