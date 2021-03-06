from rest_framework.routers import DefaultRouter 
from .views import CountryViewSet

router = DefaultRouter()

router.register(prefix='country', basename='country', viewset=CountryViewSet)

