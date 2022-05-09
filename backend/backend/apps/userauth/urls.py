from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from userauth.views import RegisterViewSet, ProfileView

router = DefaultRouter()
router.register(r'register', RegisterViewSet)

urlpatterns = [
    path('', include(router.get_urls())),
    path('login/', obtain_auth_token),
    path('profile/', ProfileView.as_view())
]
