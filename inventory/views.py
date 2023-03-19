from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, login
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
    success_url = '/ingredients'


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
    template_name = "inventory/add_item.html"


class ViewAddIngredient(CreateView):
    model = Ingredients
    form_class = AddIngredientToInventory
    template_name = "inventory/add_ingredient.html"


class ViewAddRecipe(CreateView):
    model = RecipeRequirements
    form_class = AddRecipe
    template_name = "inventory/add_recipe.html"  # configure link in template


class ViewUpdateInventory(UpdateView):
    model = Ingredients
    form_class = UpdateInventory
    template_name = ""


class SignUp(CreateView):
    model = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = ''


def logout_request(request):
    logout(request)
    return redirect('home')
