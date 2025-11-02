from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin
from .models import KnowledgePlace

@admin.register(KnowledgePlace)
class KnowledgePlaceAdmin(GISModelAdmin):
    list_display = ("name", "category", "address")
