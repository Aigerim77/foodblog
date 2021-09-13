from django.shortcuts import render, redirect
from .models import Recipe
from .forms import RecipeForm

def recipes(request):
    recipe_objects = Recipe.objects.all()[:10]
    return render(request, 'recipes/recipes.html',  {'recipes': recipe_objects})   

def create_recipe(request):
    if request.method == "POST":
        recipe_form = RecipeForm(request.POST)
        if recipe_form.is_valid():
            recipe_form.save()
            return redirect(recipes)

    recipe_form = RecipeForm()
    return render(request, 'recipes/form.html', {'recipe_form': recipe_form})

def recipe(request, id):
    recipe_object = Recipe.objects.get(id=id)
    return render(request, 'recipes/recipe.html', {'recipe_object': recipe_object})


def edit_recipe(request, id):
    recipe_object = Recipe.objects.get(id=id)
    
    if request.method == 'POST':
        recipe_form = RecipeForm(data=request.POST, instance=recipe_object)
        if recipe_form.is_valid():
            recipe_form.save()
            return redirect(recipe, id=id)

    recipe_form = RecipeForm(instance=recipe_object)
    return render(request, 'recipes/form.html', {'recipe_form': recipe_form})


def delete_recipe(request, id):
    recipe_object = Recipe.objects.get(id=id)
    recipe_object.delete()
    return redirect(recipes)




def comment(request, recipe_id):
    pass