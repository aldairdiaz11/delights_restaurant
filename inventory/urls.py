from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('ingredients/', views.ViewIngredients.as_view(), name='ingredients'),
    path('ingredients/delete/<pk>/', views.DeleteIngredients.as_view(), name="delete-ingredients"),
    path('menu/', views.ViewMenuItems.as_view(), name='menu-items'),
    path('purchase/', views.ViewPurchase.as_view(), name='purchase'),
    path('profit/', views.ViewProfit.as_view(), name='profit'),
    # Forms paths:
    path('add_ingredient/', views.ViewAddIngredient.as_view(), name='add-ingredient'),
    path('add_recipe/', views.ViewAddRecipe.as_view(), name='add-recipe'),
    path('add_item/', views.ViewAddItem.as_view(), name='add-item')
]
