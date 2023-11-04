from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    steps = models.TextField()
    preparation_time = models.PositiveIntegerField()
    image = models.ImageField(upload_to="recipe_images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredients = models.TextField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
