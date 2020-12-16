from django.urls import path, include
from rest_framework import routers

from django_csai.views import DictionaryViewSet, DocumentViewSet

router = routers.DefaultRouter()
router.register(r'dictionary', DictionaryViewSet)
router.register(r'document', DocumentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
