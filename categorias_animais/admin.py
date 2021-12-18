from django.contrib import admin
from .models import Animals, AnimalsCategory

# Register your models here.
admin.site.register(Animals)
admin.site.register(AnimalsCategory)