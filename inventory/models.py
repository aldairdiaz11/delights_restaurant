import datetime
from django.db import models


class Ingredients(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=10, default='kg')
    price = models.FloatField(default=0)

    def get_absolute_url(self):
        return '/ingredients'


class MenuItem(models.Model):
    title = models.CharField(max_length=30)
    price = models.FloatField(default=0)

    def get_absolute_url(self):
        return '/menu'


class RecipeRequirements(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredients = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)


class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(datetime.date.today)
