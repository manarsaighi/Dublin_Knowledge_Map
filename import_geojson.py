import os

import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dublin_literary_map.settings")
django.setup()

# Explicitly point to your GDAL DLL
os.environ['GDAL_LIBRARY_PATH'] = r"C:\Users\manar\literary_map\venv\Lib\site-packages\osgeo\gdal.dll"




import json
from django.contrib.gis.geos import GEOSGeometry



from places.models import KnowledgePlace

# Adjust the path to your GeoJSON
geojson_path = os.path.join("places", "knowledge_places2.geojson")


with open(geojson_path, encoding="utf-8") as f:
    data = json.load(f)

for feature in data["features"]:
    props = feature["properties"]
    geom = GEOSGeometry(json.dumps(feature["geometry"]))  

    KnowledgePlace.objects.create(
        name=props.get("name"),
        category=props.get("category"),
        address=props.get("address"),
        description=props.get("description"),
        geometry=geom  
    )

print(f"Imported {len(data['features'])} knowledge places!")
