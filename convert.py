# convert_to_geojson.py
import json
import os
import django
from django.contrib.gis.geos import GEOSGeometry

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dublin_literary_map.settings")
django.setup()

from places.models import KnowledgePlace  # Adjust app name if needed

def knowledgeplaces_to_geojson(output_file="knowledgeplaces.geojson"):
    """
    Convert all KnowledgePlace objects to Leaflet-ready GeoJSON
    and save to a file.
    """
    features = []

    for place in KnowledgePlace.objects.all():
        # Convert geometry to GEOS object if not already
        geom = place.geometry
        if isinstance(geom, str):
            geom = GEOSGeometry(geom)

        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [geom.x, geom.y]  # lon, lat
            },
            "properties": {
                "id": place.id,
                "name": place.name,
                "category": place.category,
                "address": place.address,
                "description": place.description,
            }
        }
        features.append(feature)

    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    # Save to file
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(geojson, f, ensure_ascii=False, indent=2)

    print(f"GeoJSON saved to {output_file}, total features: {len(features)}")


if __name__ == "__main__":
    knowledgeplaces_to_geojson()
