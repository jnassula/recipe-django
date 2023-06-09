from django.shortcuts import render
from utils.recipes.factory import make_recipe
from .models import Recipe

def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    return render(
        request,
        'recipes/pages/home.html',
        context={
            'recipes': recipes,
        },
    )

def category(request, category_id: int):
    recipes = Recipe.objects.filter(category__id=category_id).order_by('-id')
    return render(
        request,
        'recipes/pages/home.html',
        context={
            'recipes': recipes,
        },
    )

def recipe(request, id: int):
    return render(
        request,
        'recipes/pages/recipe-view.html',
        context={
            'recipe': make_recipe(),
            'is_recipe_details': True,
        },
    )
