from django.views.generic import ListView, TemplateView
from django.views.generic.edit import DeleteView  # CreateView, UpdateView,
from .models import Ingredients, MenuItem, RecipeRequirements, Purchase


class Home(TemplateView):
    template_name = ""


class ViewIngredients(ListView):
    model = Ingredients
    template_name = ""


class DeleteIngredients(DeleteView):
    model = Ingredients
    template_name = ""


class ViewMenuItems(ListView):
    model = MenuItem
    template_name = ""


class ViewPurchase(ListView):
    model = Purchase
    template_name = ""


class ViewProfit(ListView):
    model = RecipeRequirements
    template_name = ""
