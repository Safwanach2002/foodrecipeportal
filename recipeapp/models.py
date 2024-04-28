from django.db import models
from django.contrib.auth.models import User
import re
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Ingredient(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cook_time = models.CharField(max_length=50) 
    preparation_time = models.CharField(max_length=50)
    total_time = models.CharField(max_length=50)
    serves = models.PositiveIntegerField(default=1)
    ingredients = models.ManyToManyField(Ingredient)
    instructions = models.TextField()
    video_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def video_id(self):
        # Extract video ID from the YouTube URL using a regular expression
        if self.video_link:
            match = re.search(r"(?<=v=)[a-zA-Z0-9_-]+", self.video_link)
            if match:
                return match.group(0)
        return None

    def __str__(self):
        return self.title
    
class Review(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    """rating = models.IntegerField(choices=[
        (1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'),
        (4, '4 Stars'), (5, '5 Stars')
    ])"""
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.recipe.title}"
        #return f"{self.recipe.title} - {self.user.username}"
    