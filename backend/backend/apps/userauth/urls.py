from django.urls import path, include
from rest_framework.routers import DefaultRouter
from userauth.views import RegisterViewSet

router = DefaultRouter()
router.register(r'register', RegisterViewSet)

urlpatterns = [
    path('', include(router.get_urls()))
]
