from django.shortcuts import render, redirect
from .models import Animal
from .form import AnimalsForm


# Create your views here.
def home(request):
    animals = Animal.objects.all()
    context = {"animals": animals}
    return render(request, "home.html", context)


def create_animal(request):
    animals_form = AnimalsForm()
    if request.method == "POST":
        animals_form = AnimalsForm(request.POST)
        if animals_form.is_valid():
            animals_form.save()
            return redirect("/")

    context = {"animals_form": animals_form}
    return render(request, "cadastrar.html", context)


def update_animal(request, pk):
    animal = Animal.objects.get(id=pk)
    update_animal = AnimalsForm(instance=animal)
    if request.method == "POST":
        update_animal = AnimalsForm(request.POST, instance=animal)
        if update_animal.is_valid():
            update_animal.save()
            return redirect("/")
    context = {"update_animal": update_animal}
    return render(request, "atualizar.html", context)


def delete_animal(request, pk):
    animal = Animal.objects.get(id=pk)

    if request.method == "POST":
        animal.delete()
        return redirect("/")
    context = {"animal": animal}
    return render(request, "deletar.html", context)
