from django.shortcuts import render
from .models import Recipe

def recipes(request):
    recipe_objects = Recipe.objects.all()
    return render(request, 'recipes.html',  {'recipes': recipe_objects})   


