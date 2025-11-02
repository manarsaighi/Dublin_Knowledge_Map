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
   

    def __str__(self):
        return self.name
