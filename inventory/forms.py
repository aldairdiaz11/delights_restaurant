from django import forms
from .models import Ingredients, MenuItem, RecipeRequirements


class AddItemToMenu(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = "__all__"


class AddIngredientToInventory(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields = "__all__"


class AddRecipe(forms.ModelForm):
    class Meta:
        model = RecipeRequirements
        fields = "__all__"


class UpdateInventory(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields = "__all__"
