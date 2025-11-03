from django.urls import path
from . import views

urlpatterns = [
    # REST API (Django REST Framework)
    path('api/knowledgeplaces/', views.KnowledgePlaceListCreateView.as_view(), name='knowledgeplaces-list'),
    path('api/knowledgeplaces/<int:pk>/', views.KnowledgePlaceDetailView.as_view(), name='knowledgeplaces-detail'),

    # GeoJSON endpoint (for Leaflet)
    path('api/knowledgeplaces/geojson/', views.knowledgeplaces_geojson, name='knowledgeplaces-geojson'),

    # Map page
    path('map/', views.map_view, name='map-view'),
]
