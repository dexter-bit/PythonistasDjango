from django.shortcuts import render, redirect
from django.http import HttpResponse

from PizzeriaUCAB.models import Client, Pizza, Order, PizzaIngredient, Ingredient, PizzaOrder


# Create your views here.
itemsArray = []
isItemsArray = False

class Item:            
       def __init__(self, client, size, ingredients, price):      
               self.client = client                 
               self.size = size
               self.ingredients = ingredients                 
               self.price = price

def index(request):

    global isItemsArray
    global itemsArray

    context_dict = {
        'isItemsArray': isItemsArray,
        'itemsArray': itemsArray
    }

    return render(
        request,
        'index.html',
        context_dict
    )

def agregar(request):

    global isItemsArray

    if request.method == 'POST':
        client_name = request.POST['client_name']

        tamano_input = request.POST['tamano_input']
        jamon_input = request.POST['jamon_input']
        salami_input = request.POST['salami_input']
        queso_input = request.POST['queso_input']
        champ_input = request.POST['champ_input']
        pimenton_input = request.POST['pimenton_input']
        pepperoni_input = request.POST['pepperoni_input']
        aceituna_input = request.POST['aceituna_input']

        if tamano_input == 'Grande':
            precioTamano = 20
        elif tamano_input == 'Mediana':
            precioTamano = 16
        elif tamano_input == 'Personal':
            precioTamano = 10

        precioTotal = precioTamano + int(jamon_input)*10 + int(salami_input)*30 + int(queso_input)*30 + int(champ_input)*30 + int(pimenton_input)*30 + int(pepperoni_input)*30 + int(aceituna_input)*30
        print(client_name)
        
        cliente = Client(name=client_name)
        cliente.save()

        order = Order()
        order.client_FK = cliente
        order.save()

        pizza = Pizza(size=tamano_input, totalPrice=precioTotal)
        pizza.save()

        pizzaOrder = PizzaOrder()
        pizzaOrder.pizza_FK = pizza
        pizzaOrder.order_FK = order
        pizzaOrder.save()

        ingredientsArray = []
        if jamon_input != 0:
            ingrediente = PizzaIngredient()
            ingrediente.ingredient_FK = Ingredient.objects.get(name="Jamon")
            ingrediente.pizza_FK = pizza
            ingrediente.save()
            ingredientsArray.append(ingrediente)
        elif pimenton_input != 0:
            ingrediente = PizzaIngredient()
            ingrediente.ingredient_FK = Ingredient.objects.get(name="Pimenton")
            ingrediente.pizza_FK = pizza
            ingrediente.save()
            ingredientsArray.append(ingrediente)
        elif queso_input != 0:
            ingrediente = PizzaIngredient()
            ingrediente.ingredient_FK = Ingredient.objects.get(name="Queso")
            ingrediente.pizza_FK = pizza
            ingrediente.save()
            ingredientsArray.append(ingrediente)
        elif champ_input != 0:
            ingrediente = PizzaIngredient()
            ingrediente.ingredient_FK = Ingredient.objects.get(name="Champiñon")
            ingrediente.pizza_FK = pizza
            ingrediente.save()
            ingredientsArray.append(ingrediente)
        elif aceituna_input != 0:
            ingrediente = PizzaIngredient()
            ingrediente.ingredient_FK = Ingredient.objects.get(name="Aceitunas")
            ingrediente.pizza_FK = pizza
            ingrediente.save()
            ingredientsArray.append(ingrediente)
        elif pepperoni_input != 0:
            ingrediente = PizzaIngredient()
            ingrediente.ingredient_FK = Ingredient.objects.get(name="Pepperoni")
            ingrediente.pizza_FK = pizza
            ingrediente.save()
            ingredientsArray.append(ingrediente)
        elif salami_input != 0:
            ingrediente = PizzaIngredient()
            ingrediente.ingredient_FK = Ingredient.objects.get(name="Salami")
            ingrediente.pizza_FK = pizza
            ingrediente.save()
            ingredientsArray.append(ingrediente)

        print(ingredientsArray)

        item = Item(client=cliente, size=tamano_input, ingredients=ingredientsArray, price=precioTotal)
        itemsArray.append(item)
        isItemsArray = True

        return redirect('/')
    

def ordenar(request):

    print(request)

    return render(
        request,
        'index.html'
    )

