from django.contrib import admin
from .models import DataGather
from leaflet.admin import LeafletGeoAdmin


@admin.register(DataGather)
class DataGatherDecore(LeafletGeoAdmin):
    list_display = ("author", "title1")
    prepopulated_fields = {
        "slug": ("author", "title1", "title2")
    }
