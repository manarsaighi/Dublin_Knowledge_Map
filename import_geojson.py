import os
import django
import json
from pathlib import Path
from django.contrib.gis.geos import GEOSGeometry

# --- Django setup ---
BASE_DIR = Path(__file__).resolve().parent
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dublin_literary_map.settings")
django.setup()

from places.models import KnowledgePlace  # your model

# --- Optional: category normalization ---
CATEGORY_MAP = {
    "library": "library",
    "museum": "museum",
    "university": "university",
    "heritage": "heritage",
    "literary landmark": "heritage",
}

# --- GeoJSON file path ---
geojson_file = BASE_DIR / "places" / "static" / "places" / "knowledgeplaces.geojson"

if not geojson_file.exists():
    raise FileNotFoundError(f"GeoJSON file not found at {geojson_file}")

with open(geojson_file, encoding="utf-8") as f:
    data = json.load(f)

imported_count = 0
updated_count = 0

for feature in data.get("features", []):
    props = feature.get("properties", {})
    geometry_data = feature.get("geometry")

    if not geometry_data:
        continue  # skip if no geometry

    geom = GEOSGeometry(json.dumps(geometry_data))

    # Normalize category safely
    raw_category = props.get("category", "").strip().lower()
    category = CATEGORY_MAP.get(raw_category, "heritage")  # fallback if unknown

    obj, created = KnowledgePlace.objects.update_or_create(
        name=props.get("name", "Unknown"),
        defaults={
            "category": category,
            "address": props.get("address", ""),
            "description": props.get("description", ""),
            "geometry": geom
        }
    )

    if created:
        imported_count += 1
    else:
        updated_count += 1

print(f"Imported {imported_count} new places, updated {updated_count} existing places.")
