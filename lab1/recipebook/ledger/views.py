from django.shortcuts import render

def recipe_list(request, recipe_number=None):
    recipes = [
        {
            "name": "Recipe 1",
            "ingredients": [
                {"name": "tomato", "quantity": "3 pcs"},
                {"name": "onion", "quantity": "1 pc"},
                {"name": "pork", "quantity": "1 kg"},
                {"name": "water", "quantity": "1 L"},
                {"name": "sinigang mix", "quantity": "1 packet"}
            ],
            "link": "/recipe/1"
        },
        {
            "name": "Recipe 2",
            "ingredients": [
                {"name": "garlic", "quantity": "1 head"},
                {"name": "onion", "quantity": "1 pc"},
                {"name": "vinegar", "quantity": "1/2 cup"},
                {"name": "water", "quantity": "1 cup"},
                {"name": "salt", "quantity": "1 tablespoon"},
                {"name": "whole black peppers", "quantity": "1 tablespoon"},
                {"name": "pork", "quantity": "1 kilo"}
            ],
            "link": "/recipe/2"
        }
    ]

    context = {}

    if recipe_number is not None:
        for recipe in recipes:
            if int(recipe_number) == int(recipe['link'].split('/')[-1]):
                context['selected_recipe'] = recipe
                break

    context['recipes'] = recipes

    return render(request, 'recipe_list.html', context)
