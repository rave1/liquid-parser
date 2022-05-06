from django.urls import include, path

from rest_framework.routers import DefaultRouter
from core.views import LiquidViewSet

app_name = 'core'

router = DefaultRouter()
router.register(r'parse', LiquidViewSet, basename='parse')

urlpatterns = [
    path('', include(router.get_urls())),
]
