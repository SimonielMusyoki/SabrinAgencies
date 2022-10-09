from django.contrib import admin
from .models import Property, PropertyViews


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "country", "advert_type", "property_type"]
    list_filter = ["advert_type", "property_type", "country"]


admin.site.register(PropertyViews)
