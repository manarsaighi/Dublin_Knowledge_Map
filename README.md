#Knowledge map project

Geodjango app to visualise libraries, museums, universities and heritage sites. 

Supports the following spatial queries: Proximity to fine places near a location, buffer

# Installation and Setup

Prerequisites:
Python 3.12+
PostgreSQL with PostGIS extension enabled
Virtual environmetn

1. Clone the repository

git clone repo_url
cd literary_map


2. Create and activate a virtual environment

python -m venv venv
source venv\Scripts\activate (windows)

3. Install dependencies

pip install -r requirements.txt

4. Configure database in settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'literary_map',
        'USER': 'your username',        
        'PASSWORD': 'your password',  
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

5. Apply migrations

python manage.py makemigrations
python manage.py migrate

6. Import GeoJSON data for KnowledgePlaces and Routes

python import_geojson.py

7. Start the server

python manage.py runserver

8. Open your browser at

http://127.0.0.1:8000


## Technology Stack

**Backend:** Django, GeoDjango  
**Database:** PostgreSQL with PostGIS  
**Python Version:** 3.12+  
**Front-end:** Leaflet
**GIS libraries:** GDAL, GEOS, PROJ  

