from rest_framework import serializers
from .models import KnowledgePlace, Route

# knowledge place serialiser 


class KnowledgePlaceSerializer(serializers.ModelSerializer):
# convert model instances into json for api responses
# validate incoming data for creating/updating objects
    class Meta:
        model = KnowledgePlace # specify the  model to serialise
        fields = ['id', 'name', 'category', 'address', 'description', 'geometry'] # geometry for maps


# routes serialiser

class RouteSerializer(serializers.ModelSerializer):
# convert route objects for the route model
    class Meta:
        model = Route
        fields = ['id', 'name', 'description', 'path']
