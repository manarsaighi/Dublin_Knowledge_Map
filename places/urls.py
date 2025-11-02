from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'knowledgeplaces', views.KnowledgePlaceViewSet)

urlpatterns = [
    path('', views.map_view, name='map'),
    path('api/', include(router.urls)),   
]
