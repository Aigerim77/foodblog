from django import forms
from .models import Recipe, Feedback


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'short_description', 'description', 'img']
        

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['recipe', 'text']