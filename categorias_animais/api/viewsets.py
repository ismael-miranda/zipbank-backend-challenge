from rest_framework import viewsets
from categorias_animais.models import Animal
from categorias_animais.api.serializers import AnimalSerializer


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
