from django.db import models


# Create your models here.

class Animal(models.Model):
    name = models.CharField(max_length=150)
    life_estimate = models.IntegerField()
    food = models.CharField(max_length=100)
    CATEGORY_CHOICE = [
        ("INVERTEBRATES", "Invertebrados"),
        ("FISH", "Peixe"),
        ("AMPHIBIANS", "Anfíbios"),
        ("REPTILES", "Répteis"),
        ("BIRDS", "Aves"),
        ("MAMMALS", "Mamíferos"),
    ]
    animal_category = models.CharField(max_length=20, choices=CATEGORY_CHOICE)

    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animals"

    def __str__(self):
        return self.name
