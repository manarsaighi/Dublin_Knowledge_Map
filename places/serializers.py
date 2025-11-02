from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import KnowledgePlace

class KnowledgePlaceSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = KnowledgePlace
        geo_field = "geometry"
        fields = ('id', 'name', 'category', 'address', 'description')
