import os
import django
import json
from pathlib import Path
from django.contrib.gis.geos import GEOSGeometry

BASE_DIR = Path(__file__).resolve().parent

from pyproj import datadir
os.environ['PROJ_LIB'] = datadir.get_data_dir()
os.environ['GDAL_DATA'] = datadir.get_data_dir()


# Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dublin_literary_map.settings")
django.setup()

from places.models import KnowledgePlace

CATEGORY_MAP = {
    "Library": "library",
    "Museum": "museum",
    "University": "university",
    "Heritage": "heritage"
}

geojson_path = BASE_DIR / "places" / "static" / "places" / "knowledge_places2.geojson"
with open(geojson_path, encoding="utf-8") as f:
    data = json.load(f)


imported_count = 0

for feature in data.get("features", []):
    props = feature.get("properties", {})
    geometry_data = feature.get("geometry")
    if not geometry_data:
        continue

    geom = GEOSGeometry(json.dumps(geometry_data))

    # Normalize category
    geo_category = props.get("category")
    cat = CATEGORY_MAP.get(geo_category, "library")

    # Update existing entries or create new ones
    obj, created = KnowledgePlace.objects.update_or_create(
        name=props.get("name", "Unknown"),
        defaults={
            "category": cat,
            "address": props.get("address", ""),
            "description": props.get("description", ""),
            "geometry": geom
        }
    )

    imported_count += 1 if created else 0

print(f"Imported {imported_count} new knowledge places into the database.")
