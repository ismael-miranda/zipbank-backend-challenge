from django.db import models


# Create your models here.

class Animal(models.Model):
    CATEGORY_CHOICE = [
        ("Invertebrados", "Invertebrados"),
        ("FISH", "Peixe"),
        ("Anfíbios", "Anfíbios"),
        ("Répteis", "Répteis"),
        ("Aves", "Aves"),
        ("Mamíferos", "Mamíferos"),
    ]
    AGE = [("Dias", "Dias"), ("Meses", "Meses"), ("Anos", "Anos")]
    name = models.CharField("Nome", max_length=150, unique=True)
    food = models.CharField("Alimentação", max_length=100)
    life_estimate = models.IntegerField("Expectativa de Vida")
    animal_age = models.CharField(max_length=6, choices=AGE)
    animal_category = models.CharField("Animal Categoria", max_length=20, choices=CATEGORY_CHOICE)


    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animals"

    def __str__(self):
        return self.name
