import factory
from recipes.models import Recipe

class RecipeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Recipe

    name = factory.Sequence(lambda n: f'Recipe of recipe number {n}')
    short_description = factory.Sequence(lambda n: f'Short_description {n}')
    description = factory.Sequence(lambda n: f'Description {n}')