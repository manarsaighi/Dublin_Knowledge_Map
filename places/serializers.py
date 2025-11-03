from rest_framework import serializers
from .models import KnowledgePlace

class KnowledgePlaceSerializer(serializers.ModelSerializer):
    """Serializer for Knowledge Places"""
    class Meta:
        model = KnowledgePlace
        fields = ['id', 'name', 'category', 'address', 'description', 'geometry']
