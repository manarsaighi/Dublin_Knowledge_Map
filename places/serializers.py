from rest_framework import serializers
from .models import KnowledgePlace, Route

class KnowledgePlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = KnowledgePlace
        fields = ['id', 'name', 'category', 'address', 'description', 'geometry']

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['id', 'name', 'description', 'path']
