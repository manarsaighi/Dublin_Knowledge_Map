import os
import django

# 1️⃣ Tell Django which settings to use
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dublin_literary_map.settings")

# 2️⃣ Initialize Django
django.setup()

# 3️⃣ Now you can safely import models
from places.models import KnowledgePlace, Route
from django.contrib.gis.geos import LineString
from django.contrib.gis.db.models.functions import Distance

categories = {
    'library': 'Library Route',
    'museum': 'Museum Route',
    'heritage': 'Heritage Route',
    'university': 'College Route',
}

for category, route_name in categories.items():
    starting_place = KnowledgePlace.objects.filter(category=category).first()
    if not starting_place:
        print(f"No places for {route_name}")
        continue

    start_point = starting_place.geometry
    nearby_places = KnowledgePlace.objects.filter(category=category).annotate(
        distance=Distance('geometry', start_point)
    ).order_by('distance')[:5]

    if nearby_places.count() < 2:
        print(f"Not enough places to create {route_name}")
        continue

    coords = [(p.geometry.x, p.geometry.y) for p in nearby_places]
    line = LineString(coords, srid=4326)

    Route.objects.update_or_create(
        name=route_name,
        defaults={'path': line, 'description': f"Route connecting {category} locations"}
    )

    print(f"{route_name} created/updated with {len(coords)} points")
