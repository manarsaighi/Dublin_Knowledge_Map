from django.shortcuts import render
from rest_framework import viewsets
from .models import KnowledgePlace
from .serializers import KnowledgePlaceSerializer

def map_view(request):
    return render(request, "places/map.html")

class KnowledgePlaceViewSet(viewsets.ModelViewSet):
    queryset = KnowledgePlace.objects.all()
    serializer_class = KnowledgePlaceSerializer
