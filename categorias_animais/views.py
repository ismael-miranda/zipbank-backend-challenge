from django.shortcuts import render
from .models import Animals, AnimalsCategory
from .form import AnimalsForm, AnimalsCategoryForm


# Create your views here.
def home(request):
    animals = Animals.objects.all()
    context = {"animals": animals}
    return render(request, "home.html", context)



