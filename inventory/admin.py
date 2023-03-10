from django.contrib import admin
from .models import Ingredients, MenuItem, RecipeRequirements, Purchase

admin.site.register(Ingredients)
admin.site.register(MenuItem)
admin.site.register(RecipeRequirements)
admin.site.register(Purchase)
