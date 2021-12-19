from django.forms import ModelForm
from .models import Animal


class AnimalsForm(ModelForm):
    class Meta:
        model = Animal
        fields = "__all__"
