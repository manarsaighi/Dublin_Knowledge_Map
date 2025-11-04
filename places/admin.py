from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin
from .models import KnowledgePlace
from .models import Route


# knowledge place admin
@admin.register(KnowledgePlace)
class KnowledgePlaceAdmin(GISModelAdmin):
    list_display = ("name", "category", "address")
    list_filter = ("category",)
    search_fields = ("name", "address", "description")
    
# routes admin
@admin.register(Route)
class RouteAdmin(GISModelAdmin):
    list_display = ("name",)
    search_fields = ("name", "description")
 