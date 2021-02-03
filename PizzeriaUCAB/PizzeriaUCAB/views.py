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

###from .forms import CheckoutForm, CouponForm, RefundForm, PaymentForm
from .models import Pizza, PizzaIngredient, Ingredient, PizzaOrder, Client
from .forms import PizzaForm

def products(request):
    return render(request, 'pizza.html')

class Ingredient(View):
    def get(self,request):
        form = PizzaForm(request.POST or None)        
        
        context={
            'form':form,
            #'ingredients':Ingredient.objects.all(),
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

class Pizza(View):
    def get(self,request):
        form = PizzaForm(request.POST or None)        
        
        context={
            'form':form,
            #'Pizzas':Pizza.objects.all(),
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
            #'orders':Order.objects.all(),
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
