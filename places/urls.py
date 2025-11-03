from django.urls import path
from . import views

urlpatterns = [
    # KnowledgePlace CRUD + GeoJSON
    path('api/knowledgeplaces/', views.KnowledgePlaceListCreateView.as_view(), name='knowledgeplace-list'),
    path('api/knowledgeplaces/<int:pk>/', views.KnowledgePlaceDetailView.as_view(), name='knowledgeplace-detail'),
    path('api/knowledgeplaces/geojson/', views.knowledgeplaces_geojson, name='knowledgeplaces-geojson'),
    path('api/knowledgeplaces/within_radius/', views.places_within_radius, name='places-within-radius'),

    # Route CRUD + GeoJSON
    path('api/routes/', views.RouteListCreateView.as_view(), name='route-list'),
    path('api/routes/<int:pk>/', views.RouteDetailView.as_view(), name='route-detail'),
    path('api/routes/geojson/', views.routes_geojson, name='routes-geojson'),

     path(
        'api/routes/intersect-place/<int:place_id>/',
        views.routes_intersect_place,
        name='routes-intersect-place'
    ),
    # Map template
    path('', views.map_view, name='map-view'),
]
