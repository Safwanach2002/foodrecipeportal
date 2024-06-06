from django import forms
from .models import Recipe, Category, Ingredient, Review #forms

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'image' , 'category', 'cook_time', 'preparation_time' , 'total_time' ,'serves', 'ingredients', 'instructions', 'video_link']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'rating']
        labels = {
            'content': 'Your Review',
            'rating': 'Rating'
        }
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
            'rating': forms.Select(choices=[(i, i) for i in range(1, 6)]),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name']

class SearchForm(forms.Form):
    search_query = forms.CharField(label='Search any recipe', max_length=100)
    #search_query = forms.CharField(max_length=100, label='Search')
