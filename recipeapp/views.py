from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from .models import Recipe, Category, Ingredient, Review
from .forms import RecipeSearchForm, ReviewForm
from rest_framework import generics
from django.db.models import Avg
from .serializers import CategorySerializer, IngredientSerializer, RecipeSerializer, ReviewSerializer
from django.contrib.auth.decorators import login_required

from recipeapp import models

# Create your views here.

def home(request):
    return render (request,'index.html')

def new_recipes(request):
    return render(request, 'new_recipes.html')

def ingredients(request):
    return render(request, 'ingredient_detail.html')

def about(request):
    return render(request, 'about.html')

def about_viewmore(request):
    return render(request, 'about_viewmore.html')

def search_results(request):
    if request.method == 'GET':
        search_form = RecipeSearchForm(request.GET)

        if search_form.is_valid():
            search_query = search_form.cleaned_data['search_query']
            recipes = Recipe.objects.filter(title__icontains=search_query)

        return render(request, 'search_results.html', {'search_form': search_form, 'recipes': recipes})

    return render(request, 'search_results.html', {'search_form': search_form})

        
def chicken(request):
    return render(request, 'chicken.html')

def beef(request):
    return render(request, 'beef.html')

def seafood(request):
    return render(request, 'seafood.html')

def fruits(request):
    return render(request, 'fruits.html')

def vegetables(request):
    return render(request, 'vegetables.html')

def indianfood(request):
    return render(request, 'indianfood.html')

def chinesefood(request):
    return render(request, 'chinesefood.html')

def italianfood(request):
    return render(request, 'italianfood.html')

def mexicanfood(request):
    return render(request, 'mexicanfood.html')

def koreanfood(request):
    return render(request, 'koreanfood.html')

def spanishfood(request):
    return render(request, 'koreanfood.html')

def japanesefood(request):
    return render(request, 'japanesefood.html')

def vietnamesefood(request):
    return render(request, 'vietnamesefood.html')

class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class IngredientListCreate(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class RecipeListCreate(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class ReviewListCreate(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


def recipe_detail_view(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    reviews = recipe.review_set.all()

    for review in reviews:
        review.rating_stars = range(review.rating)
        review.empty_stars = range(5 - review.rating)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.recipe = recipe
            review.save()
            return redirect('recipe_detail', pk=pk)
    else:
        form = ReviewForm()
    return render(request, 'recipe_detail.html', {'recipe': recipe, 'reviews': reviews, 'form': form})

def get_recipe(request):
    recipe_id = request.GET.get('recipe_id')
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    # Render the recipe details using a template
    context = {'recipe': recipe}
    return render(request, 'recipe_details.html', context)

''''@login_required
def add_review(request):
    if request.method == 'POST':
        # Process the form data and save the review
        # Example code:
        title = request.POST.get('review_title')
        content = request.POST.get('review_content')
        rating = request.POST.get('review_rating')
        recipe_id = request.POST.get('recipe_id')

        review = Review(title=title, content=content, rating=rating, recipe_id=recipe_id, user=request.user)
        review.save()
        return redirect('recipe_detail', recipe_id=recipe_id)  # Redirect to the recipe detail page

    # Handle GET request or other cases
    return render(request, 'index.html', context={})  # Repla'''


@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.recipe_id = request.POST.get('recipe_id')            
            review.save()
            return redirect('recipe_detail', pk=review.recipe.pk)
    else:
        form = ReviewForm()

    recipe_id = request.POST.get('recipe_id')  # Ensure recipe_id is passed to the template
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    context = {'recipe': recipe, 'form': form}
    return render(request, 'recipe_detail.html', context)
    
    #return render(request, 'add_review.html', {'form': form})
