from django.urls import path
from .views import home, create_animal, update_animal, delete_animal

urlpatterns = [
    path("", home, name="home"),
    path("cadastrar/", create_animal, name="cadastrar"),
    path("atualizar/<int:pk>/", update_animal, name="atualizar"),
    path("deletar/<int:pk>/", delete_animal, name="deletar"),
]
