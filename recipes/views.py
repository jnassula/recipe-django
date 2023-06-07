from django.shortcuts import render
from utils.recipes.factory import make_recipe

def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(6)],
        })


def recipe(request, id: int):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_recipe_details': True,
        })
