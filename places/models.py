from django.contrib.gis.db import models


# representing a knowledge related place (library, museum, university, heritage site)
class KnowledgePlace(models.Model):
# choices for category field
    CATEGORY_CHOICES = [
        ('library', 'Library'),
        ('museum', 'Museum'),
        ('university', 'University'),
        ('heritage', 'Heritage'),
    ]

# place name, category, address, geographic location
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    address = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    geometry = models.PointField(srid=4326, spatial_index=True)

    class Meta:
        db_table = 'places_knowledgeplace' # database table to hold the content
        verbose_name = "Knowledge Place" # human readable names
        verbose_name_plural = "Knowledge Places"
        ordering = ['name']

    def __str__(self):
        return self.name


# route model

class Route(models.Model):
    # name of the route, desc, geographic path
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    path = models.LineStringField(srid=4326)

    class Meta:
        db_table = 'routes'# database table for routes content
        verbose_name = "Route"
        verbose_name_plural = "Routes"
        ordering = ['name']

    def __str__(self):
        return self.name
