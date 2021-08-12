from django.test import TestCase
from django.urls import reverse
from django.db.models import QuerySet
from .factories import RecipeFactory

class RecipeListTestCase(TestCase):
    def test_open_list_success(self):
        recipe_1 = RecipeFactory()
        recipe_2 = RecipeFactory()

        url = reverse('recipes-list')
        response = self.client.get('/recipes/')
        self.assertEqual(response.status_code, 200)
        recipes = response.context.get('recipes')
        self.assertIsInstance(recipes, QuerySet)
        print(recipes)


