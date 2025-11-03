from rest_framework import generics
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.shortcuts import render
from .models import KnowledgePlace, Route
from .serializers import KnowledgePlaceSerializer, RouteSerializer
import json


class KnowledgePlaceListCreateView(generics.ListCreateAPIView):
    """List all KnowledgePlaces or create a new one"""
    queryset = KnowledgePlace.objects.all()
    serializer_class = KnowledgePlaceSerializer

class KnowledgePlaceDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update, or delete a KnowledgePlace"""
    queryset = KnowledgePlace.objects.all()
    serializer_class = KnowledgePlaceSerializer

@api_view(['GET'])
def knowledgeplaces_geojson(request):
    """Return KnowledgePlace data as GeoJSON for Leaflet"""
    places = KnowledgePlace.objects.all()
    features = []
    for place in places:
        if not place.geometry:
            continue
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.geometry.x, place.geometry.y],
            },
            "properties": {
                "id": place.id,
                "name": place.name,
                "category": place.category,
                "address": place.address or "",
                "description": place.description or "",
            },
        })
    return JsonResponse({"type": "FeatureCollection", "features": features})


class RouteListCreateView(generics.ListCreateAPIView):
    """List or create Routes"""
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

class RouteDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update, or delete a Route"""
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

@api_view(['GET'])
def routes_geojson(request):
    """Return Routes as GeoJSON for Leaflet"""
    routes = Route.objects.all()
    features = []
    for route in routes:
        if not route.path:
            continue
        features.append({
            "type": "Feature",
            "geometry": json.loads(route.path.geojson),
            "properties": {
                "id": route.id,
                "name": route.name,
                "description": route.description or "",
            },
        })
    return JsonResponse({"type": "FeatureCollection", "features": features})

def map_view(request):
    """Render the Leaflet map"""
    return render(request, 'places/map.html')
