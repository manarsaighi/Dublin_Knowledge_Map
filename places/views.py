from rest_framework import generics
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.shortcuts import render
from .models import KnowledgePlace
from .serializers import KnowledgePlaceSerializer


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

        feature = {
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
        }
        features.append(feature)

    geojson = {
        "type": "FeatureCollection",
        "features": features,
    }

    return JsonResponse(geojson)


def map_view(request):
    """Render the Leaflet map"""
    return render(request, 'places/map.html')
