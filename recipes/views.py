from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from .models import Recipe, Category
from .forms import RecipeForm


def home(request):
    first_courses = Recipe.objects.filter(categories__name="Первые блюда")
    second_courses = Recipe.objects.filter(categories__name="Вторые блюда")
    salads = Recipe.objects.filter(categories__name="Салаты")
    desserts = Recipe.objects.filter(categories__name="Десерты")

    context = {
        "first_courses": first_courses,
        "second_courses": second_courses,
        "salads": salads,
        "desserts": desserts,
    }

    return render(request, "home.html", context)


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    context = {"recipe": recipe}
    return render(request, "recipe_detail.html", context)


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()

    context = {"form": form}
    return render(request, "register.html", context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()

    context = {"form": form}
    return render(request, "login.html", context)


def logout(request):
    auth_logout(request)
    return redirect("home")


def add_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            new_recipe = form.save(commit=False)
            new_recipe.author = request.user
            new_recipe.save()
            form.save_m2m()
            return redirect("home")
    else:
        form = RecipeForm()

    context = {"form": form}
    return render(request, "add_recipe.html", context)


def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("recipe_detail", recipe_id=recipe_id)
    else:
        form = RecipeForm(instance=recipe)

    context = {"form": form, "recipe": recipe}
    return render(request, "edit_recipe.html", context)
