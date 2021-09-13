from django.urls import path
from .views import recipes, create_recipe, recipe, \
    edit_recipe, delete_recipe, comment



urlpatterns = [
    path('', recipes, name='recipes-list'),
    path('create/', create_recipe, name='create-recipe'),
    path('<int:id>/', recipe, name='recipe'),
    path('<int:id>/edit/', edit_recipe, name='edit-recipe'),
    path('<int:id>/delete/', delete_recipe, name='delete-recipe'),
    path('<int:id>/comment/', comment, name='comment'),
]

