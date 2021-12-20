from django.urls import path, include
from .views import home, create_animal, update_animal, delete_animal
from categorias_animais.api.viewsets import AnimalViewSet
from rest_framework import routers

route = routers.DefaultRouter()
route.register(r"animais", AnimalViewSet, basename="Animais")
urlpatterns = [
    path("", home, name="home"),
    path("cadastrar/", create_animal, name="cadastrar"),
    path("atualizar/<int:pk>/", update_animal, name="atualizar"),
    path("deletar/<int:pk>/", delete_animal, name="deletar"),
    path("api/", include(route.urls)),
]
