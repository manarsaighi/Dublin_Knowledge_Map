from django.urls import path
from . import views

urlpatterns = [
 
    path('api/knowledgeplaces/', views.KnowledgePlaceListCreateView.as_view(), name='knowledgeplaces-list'),
    path('api/knowledgeplaces/<int:pk>/', views.KnowledgePlaceDetailView.as_view(), name='knowledgeplaces-detail'),
    path('api/knowledgeplaces/geojson/', views.knowledgeplaces_geojson, name='knowledgeplaces-geojson'),


    path('api/routes/', views.RouteListCreateView.as_view(), name='routes-list'),
    path('api/routes/<int:pk>/', views.RouteDetailView.as_view(), name='routes-detail'),
    path('api/routes/geojson/', views.routes_geojson, name='routes-geojson'),

    path('map/', views.map_view, name='map-view'),
]
