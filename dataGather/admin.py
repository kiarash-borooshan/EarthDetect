from django.contrib import admin
from .models import DataGather
# from leaflet.admin import LeafletGeoAdmin


@admin.register(DataGather)
class DataGatherDecore(admin.ModelAdmin):
    list_display = ("author", "title1")
    prepopulated_fields = {
        "slug": ("author", "title1", "title2")
    }
# eafletGeoAdmin):
#     list_display = ("author", "title1")
#     prepopulated_fields = {
#         "slug": ("author", "title1", "title2")
#     }
