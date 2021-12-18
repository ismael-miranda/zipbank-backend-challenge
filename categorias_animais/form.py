from django.forms import ModelForm
from .models import Animals, AnimalsCategory


class AnimalsForm(ModelForm):
    class Meta:
        model = Animals
        fields = "__all__"


class AnimalsCategoryForm(ModelForm):
    class Meta:
        model = AnimalsCategory
        fields = "__all__"
