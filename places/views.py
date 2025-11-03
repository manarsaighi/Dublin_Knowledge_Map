from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import KnowledgePlace, Route
from .serializers import KnowledgePlaceSerializer, RouteSerializer
import json


class KnowledgePlaceListCreateView(generics.ListCreateAPIView):
    queryset = KnowledgePlace.objects.all()
    serializer_class = KnowledgePlaceSerializer

class KnowledgePlaceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = KnowledgePlace.objects.all()
    serializer_class = KnowledgePlaceSerializer


@api_view(['GET'])
def knowledgeplaces_geojson(request):
    places = KnowledgePlace.objects.all()
    features = [{
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [p.geometry.x, p.geometry.y]
        },
        "properties": {
            "id": p.id,
            "name": p.name,
            "category": p.category,
            "address": p.address or "",
            "description": p.description or ""
        }
    } for p in places]
    return JsonResponse({"type": "FeatureCollection", "features": features})


class RouteListCreateView(generics.ListCreateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

class RouteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

@api_view(['GET'])
def routes_geojson(request):
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


@api_view(['GET'])
def places_within_radius(request):
    """
    Return KnowledgePlaces within a given radius (meters) of a point.
    Example: /api/knowledgeplaces/within_radius/?lat=53.3498&lon=-6.2603&radius=50
    """
    try:
        lat = float(request.GET.get('lat'))
        lon = float(request.GET.get('lon'))
    except (TypeError, ValueError):
        return Response({"error": "lat and lon parameters are required and must be numbers"}, status=400)

    radius = float(request.GET.get('radius', 500))  
    center = Point(lon, lat, srid=4326)

    # Annotate distance and filter by radius
    places = KnowledgePlace.objects.annotate(
        distance=Distance('geometry', center)
    ).filter(distance__lte=radius).order_by('distance')

    serializer = KnowledgePlaceSerializer(places, many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# def routes_intersect_place(request, place_id):
#     """Return all routes that intersect a given place"""
#     place = get_object_or_404(KnowledgePlace, id=place_id)
#     routes = Route.objects.filter(path__intersects=place.geometry)
#     serializer = RouteSerializer(routes, many=True)
#     return Response(serializer.data)

@api_view(['GET'])
def places_near_route(request, route_id):
    """
    Return KnowledgePlaces within a buffer distance of a route.
    Example: /api/routes/places-near/1/?buffer=50
    """
    buffer_distance = float(request.GET.get('buffer', 50))  # default 50 meters
    route = get_object_or_404(Route, id=route_id)

    if not route.path:
        return Response([])  # no path geometry

    # Filter places within buffer
    places = KnowledgePlace.objects.filter(
        geometry__distance_lte=(route.path, D(m=buffer_distance))
    )

    serializer = KnowledgePlaceSerializer(places, many=True)
    return Response(serializer.data)


def map_view(request):
    """Render the Leaflet map template"""
    return render(request, 'places/map.html')
