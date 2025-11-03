# import_routes.py
import os
import django
import json
from pathlib import Path
from django.contrib.gis.geos import GEOSGeometry

# --- Django setup ---
BASE_DIR = Path(__file__).resolve().parent
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dublin_literary_map.settings")
django.setup()

from places.models import Route  # adjust app name if needed

# --- GeoJSON file path ---
geojson_file = BASE_DIR / "places" / "static" / "places" / "routes.geojson"

if not geojson_file.exists():
    raise FileNotFoundError(f"GeoJSON file not found at {geojson_file}")

with open(geojson_file, encoding="utf-8") as f:
    data = json.load(f)

for feature in data.get("features", []):
    geom = GEOSGeometry(json.dumps(feature["geometry"]))
    Route.objects.update_or_create(
        name=feature["properties"]["name"],
        defaults={
            "description": feature["properties"].get("description", ""),
            "path": geom
        }
    )

print("Routes imported successfully!")
