from django.test import TestCase
from django.urls import reverse
from django.db.models import Queryset
from recipes.models import Recipe
from .factories import RecipeFactory

class RecipeListTestCase(TestCase):
    def test_open_list_success(self):
        recipe_1 = RecipeFactory()
        recipe_2 = RecipeFactory()

        url = reverse('recipes-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        recipes = response.context.get('recipes')
        self.assertIsInstance(recipes, Queryset)

        place_2_db = Place.object.get(name='Recipe number 1')
        self.assertEqual(recipe_2_db.name, recipes[1].name)

class RecipeCreateTestCase(TestCase):
    def test_creta_recipe_success(self):
        url = reverse('create-recipe')
        data = {
            'name': 'Bread',
            'short_description': 'Bread',
            'description': 'bread'
        }
        response = self.client.post(url, data)
        recipe = Recipe.object.last()
        self.assertEqual(recipe.name, 'Bread')




