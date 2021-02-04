import random
import string
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView, View
from django_datatables_view.base_datatable_view import BaseDatatableView

###from .forms import CheckoutForm, CouponForm, RefundForm, PaymentForm
from .models import Pizza as PizzaModel, PizzaIngredient, Ingredient as IngredientModel, PizzaOrder, Client, Order as OrderModel
from .forms import PizzaForm
from django.db import connection

def my_custom_sql(self):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
        cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
        row = cursor.fetchone()

    return row

def products(request):
    return render(request, 'pizza.html')

    #return row
    #pizzas vendidas
    #ingredientes de esas pizzas
    #precio de la pizza
    #quien pidio la pizza

    #ingredientes disponibles

    #clientes registrados

    #ordenes registradas

class Ingredient(View):
    def get(self,request):
        form = PizzaForm(request.POST or None)
        #with connection.cursor() as cursor:
        #    cursor.execute('''SELECT * FROM Pizza as P,Ingredient as I,PizzaIngredient as PI,Client as C,Order as O,PizzaOrder as PO WHERE O.id=PO.order_FK and PO.pizza_FK = P.id and P.id=PI.pizza_FK and PI.ingredient_FK=I.id''')
        #    row1 = cursor.fetchone()

        pos = PizzaOrder.objects.all()
        pis = PizzaIngredient.objects.all()
        pizzas = PizzaModel.objects.all()
        ingredients = IngredientModel.objects.all()
        clients = Client.objects.all()
        orders = OrderModel.objects.all()
        context={
            'form':form,
            'ingredients':ingredients,
            'clients':clients,
            'orders':orders,
            'pizzas':pizzas,
            'form':form,
            'pis':pis,
            'pos':pos
        }
        print(IngredientModel.objects.all())
        return render(
            self.request,
            'reports.html',
            context
        )
    def post(self,request):
        form = PizzaForm(request.POST or None)
        if form.is_valid():
            form.save()
        context={
            'form':form,
        }
        return render(
            self.request,
            'pizza.html',
            context
        )

class Pizza(View):
    def get(self,request):
        form = PizzaForm(request.POST or None)        
        
        context={
            'form':form,
            'pizzas':PizzaModel.objects.all()
        }
        return render(
            self.request,
            'pizza.html',
            context
        )

    def post(self,request):
        form = PizzaForm(request.POST or None)
        if form.is_valid():
            form.save()
        context={
            'form':form,
        }
        return render(
            self.request,
            'pizza.html',
            context
        )

class Order(View):
    def get(self,request):
        form = PizzaForm(request.POST or None)        
        
        context={
            'form':form,
            'orders':OrderModel.objects.all(),
        }
        return render(
            self.request,
            'index.html',
            context
        )

    def post(self,request):
        form = PizzaForm(request.POST or None)
        if form.is_valid():
            form.save()
        context={
            'form':form,
        }
        return render(
            self.request,
            'pizza.html',
            context
        )

