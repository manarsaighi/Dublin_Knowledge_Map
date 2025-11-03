from django.contrib.gis.db import models

class KnowledgePlace(models.Model):
    CATEGORY_CHOICES = [
        ('library', 'Library'),
        ('museum', 'Museum'),
        ('university', 'University or College'),
        ('heritage', 'Heritage or Literary Landmark'),
    ]

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    address = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    geometry = models.PointField(srid=4326)

    class Meta:
        db_table = 'places_knowledgeplace'
        verbose_name = "Knowledge Place"
        verbose_name_plural = "Knowledge Places"
        ordering = ['name']

    def __str__(self):
        return self.name


class Route(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    path = models.LineStringField(srid=4326)

    class Meta:
        db_table = 'routes'
        verbose_name = "Route"
        verbose_name_plural = "Routes"
        ordering = ['name']

    def __str__(self):
        return self.name
