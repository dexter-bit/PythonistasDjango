from django.shortcuts import render, redirect
from django.http import HttpResponse

from PizzeriaUCAB.models import Client, Pizza, Order, PizzaIngredient, Ingredient, PizzaOrder


# Create your views here.


def index(request):

    return render(
        request,
        'index.html'
    )

def agregar(request):

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

        if jamon_input != 0:
            ingrediente = PizzaIngredient()
            ingrediente.ingredient_FK = Ingredient.objects.get(name="Jamon")
            ingrediente.pizza_FK = pizza
            ingrediente.save()
        elif pimenton_input != 0:
            ingrediente = PizzaIngredient()
            ingrediente.ingredient_FK = Ingredient.objects.get(name="Pimenton")
            ingrediente.pizza_FK = pizza
            ingrediente.save()
        elif queso_input != 0:
            ingrediente = PizzaIngredient()
            ingrediente.ingredient_FK = Ingredient.objects.get(name="Queso")
            ingrediente.pizza_FK = pizza
            ingrediente.save()
        elif champ_input != 0:
            ingrediente = PizzaIngredient()
            ingrediente.ingredient_FK = Ingredient.objects.get(name="Champiñon")
            ingrediente.pizza_FK = pizza
            ingrediente.save()
        elif aceituna_input != 0:
            ingrediente = PizzaIngredient()
            ingrediente.ingredient_FK = Ingredient.objects.get(name="Aceitunas")
            ingrediente.pizza_FK = pizza
            ingrediente.save()
        elif pepperoni_input != 0:
            ingrediente = PizzaIngredient()
            ingrediente.ingredient_FK = Ingredient.objects.get(name="Pepperoni")
            ingrediente.pizza_FK = pizza
            ingrediente.save()
        elif salami_input != 0:
            ingrediente = PizzaIngredient()
            ingrediente.ingredient_FK = Ingredient.objects.get(name="Salami")
            ingrediente.pizza_FK = pizza
            ingrediente.save()

        print(tamano_input)
        print(jamon_input)
        print(salami_input)
        print(queso_input)
        print(champ_input)
        print(pimenton_input)
        print(pepperoni_input)
        print(aceituna_input)

        return redirect('/')
    

def ordenar(request):

    print(request)

    return render(
        request,
        'index.html'
    )

