from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("recipe/<int:recipe_id>/", views.recipe_detail, name="recipe_detail"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("add_recipe/", views.add_recipe, name="add_recipe"),
    path("edit_recipe/<int:recipe_id>/", views.edit_recipe, name="edit_recipe"),
]
