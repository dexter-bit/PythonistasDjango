from django.db import models
from django.conf import settings

class Pizza(models.Model):
	def __str__(self):
		return self.totalPrice

	objects = models.Manager()
	totalPrice = models.IntegerField(
		default=0
	)

	size = models.CharField(
		max_length=50
	)

class Ingredient(models.Model):
	def __str__(self):
		return self.name

	objects = models.Manager()
	name = models.CharField(
		max_length=50
	)

	price = models.IntegerField(
		default=0
	)

class PizzaIngredient(models.Model):
	pizza_FK = models.ForeignKey(
		Pizza,
		on_delete=models.CASCADE
	)

	ingredient_FK = models.ForeignKey(
		Ingredient,
		on_delete=models.CASCADE
	)

class Client(models.Model):
	name = models.CharField(
		max_length=50
	)

class Order(models.Model):
	client_FK = models.ForeignKey(
		Client,
		on_delete=models.CASCADE
	)


class PizzaOrder(models.Model):
	pizza_FK = models.ForeignKey(
		Pizza,
		on_delete=models.CASCADE
	)
	
	order_FK = models.ForeignKey(
		Order,
		on_delete=models.CASCADE
	)