from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('actors', views.ActorView)
router.register('directors', views.DirectorView)
router.register('movies', views.MovieView)

urlpatterns = [
  path('', include(router.urls))
]