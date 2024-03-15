from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class Ingredient(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:recipe_detail', args=[str(self.pk)])


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=200)
    ingredient = models.ForeignKey(
        'Ingredient', 
        on_delete=models.CASCADE
    )

    recipe = models.ForeignKey(
        'Recipe', 
        on_delete=models.CASCADE, 
        related_name='ingredients'
    )

    def __str__(self):
        return f"{self.quantity} of {self.ingredient.name}"