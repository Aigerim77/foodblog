from django.shortcuts import render, redirect
from django.views.generic import FormView, DetailView, ListView
from .models import Recipe, Feedback
from core.models import Advice, News
from .forms import RecipeForm, FeedbackForm
from django.db.models import Q
from itertools import chain


def recipes(request):
    recipe_objects = Recipe.objects.all()[:30]
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



class FeedbackView(FormView):
    template_name = 'recipes/feedback_form.html'
    form_class = FeedbackForm
    success_url = '/recipes/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class FeedbackDetailView(DetailView):
    queryset = Feedback.objects.all()
    template_name = 'recipes/feedback.html'



class Search(ListView):
    model = Recipe.objects.all
    template_name = 'recipes/search.html'
    
    def get_queryset(self): 
        query = self.request.GET.get('q')
        recipe = Recipe.objects.filter(
            Q(name__icontains=query) | Q(short_description__icontains=query)
            )
        advice = Advice.objects.filter(
            Q(title__icontains=query) | Q(short_description__icontains=query)
            )
        news = News.objects.filter(
            Q(title__icontains=query) | Q(short_description__icontains=query)
            )
        results = chain(recipe, advice, news)
        return results

