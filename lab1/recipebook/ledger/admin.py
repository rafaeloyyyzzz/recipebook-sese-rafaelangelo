from django.contrib import admin

from .models import Recipe, RecipeIngredient


class RecipeIngredientInLine(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInLine,]


class RecipeIngredientAdmin(admin.ModelAdmin):
      ist_display = ('quantity', 'ingredient', 'recipe')

admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)