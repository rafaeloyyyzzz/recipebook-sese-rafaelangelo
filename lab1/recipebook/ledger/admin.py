from django.contrib import admin
from .models import Recipe, RecipeIngredient, Ingredient


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline, ]
    list_display = ('name', 'author', 'created_on', 'updated_on')


class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('quantity', 'ingredient', 'recipe')


admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(Ingredient)
admin.site.register(Recipe, RecipeAdmin)