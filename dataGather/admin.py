from django.contrib import admin
from .models import DataGather


@admin.register(DataGather)
class DataGatherDecore(admin.ModelAdmin):
    list_display = ("author", "title1")
    prepopulated_fields = {
        "slug": ("author", "title1", "title2")
    }
