from django.views.generic import ListView, TemplateView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from .models import Ingredients, MenuItem, RecipeRequirements, Purchase
from .forms import AddItemToMenu, AddIngredientToInventory, AddRecipe, UpdateInventory


class Home(TemplateView):
    template_name = "inventory/home.html"


class ViewIngredients(ListView):
    model = Ingredients
    template_name = "inventory/ingredients.html"


class DeleteIngredients(DeleteView):
    model = Ingredients
    template_name = "inventory/delete_ingredient.html"


class ViewMenuItems(ListView):
    model = MenuItem
    template_name = "inventory/menu.html"


class ViewPurchase(ListView):
    model = Purchase
    template_name = "inventory/purchases.html"


class ViewProfit(ListView):
    model = RecipeRequirements
    template_name = "inventory/profit.html"


class ViewAddItem(CreateView):
    model = MenuItem
    form_class = AddItemToMenu
    template_name = ""


class ViewAddIngredient(CreateView):
    model = Ingredients
    form_class = AddIngredientToInventory
    template_name = ""


class ViewAddRecipe(CreateView):
    model = RecipeRequirements
    form_class = AddRecipe
    template_name = ""


class ViewUpdateInventory(UpdateView):
    model = Ingredients
    form_class = UpdateInventory
    template_name = ""
