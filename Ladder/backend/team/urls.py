from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('team', TeamViewset, basename='team')
urlpatterns = router.urls





