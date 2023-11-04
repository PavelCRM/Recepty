from django.contrib import admin
from .models import Recipe, Category


class RecipeAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "preparation_time")
    search_fields = ["title", "author__username"]

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category)
