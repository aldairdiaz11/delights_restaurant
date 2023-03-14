from django.views.generic import ListView, TemplateView
from django.views.generic.edit import DeleteView  # CreateView, UpdateView,
from .models import Ingredients, MenuItem, RecipeRequirements, Purchase


class Home(TemplateView):
    template_name = "inventory/home.html"


class ViewIngredients(ListView):
    model = Ingredients
    template_name = "inventory/ingredients.html"


class DeleteIngredients(DeleteView):
    model = Ingredients
    template_name = ""


class ViewMenuItems(ListView):
    model = MenuItem
    template_name = "inventory/menu.html"


class ViewPurchase(ListView):
    model = Purchase
    template_name = "inventory/purchases.html"


class ViewProfit(ListView):
    model = RecipeRequirements
    template_name = "inventory/profit.html"
