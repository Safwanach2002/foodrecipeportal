"""from django.contrib import admin
from .models import Category, Ingredient, Recipe, Review
from .forms import ReviewForm
# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'cook_time', 'created_at']
    search_fields = ['title', 'category__name']
    list_filter = ['category', 'created_at']
    form = ReviewForm

class ReviewAdmin(admin.ModelAdmin):
    form = ReviewForm

admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Review, ReviewAdmin)"""

from django.contrib import admin
from .models import Recipe, Category, Ingredient, Review
from .forms import RecipeForm, CategoryForm, IngredientForm, ReviewForm

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1 

class RecipeAdmin(admin.ModelAdmin):
    form = RecipeForm
    list_display = ('title', 'category', 'cook_time', 'preparation_time', 'total_time', 'serves', 'video_link_display', 'created_at')
    search_fields = ['title', 'category__name']
    list_filter = ['category', 'created_at']
    inlines = [ReviewInline]

    def video_link_display(self, obj):
        return obj.video_link if obj.video_link else "N/A"

    video_link_display.short_description = 'Video Link'

class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm

class IngredientAdmin(admin.ModelAdmin):
    form = IngredientForm

class ReviewAdmin(admin.ModelAdmin):
    form = ReviewForm

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Review, ReviewAdmin)
