from django import forms
from .models import Pizza, PizzaIngredient, Ingredient, PizzaOrder, Client

class PizzaForm(forms.Form):
	class Meta:
		model = Ingredient,
		fields=[
			'name',
			'price'
		]
	shipping_address = forms.CharField(required=False)
	shipping_address2 = forms.CharField(required=False)