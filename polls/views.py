from django.shortcuts import render, redirect, get_object_or_404
from .models import Sight, Type, Item
from django.views.generic import ListView,DetailView
from cart.forms import CartAddItemForm
#def index(request):
    #sights = Sight.objects.all()
    #return render(request,'home.html', {'sights':sights})
class HomeView(ListView):
    model = Sight
    template_name = "home.html"

class SightDatailView(DetailView):
    model = Sight
    template_name = "sight_one.html"

class PricesView(ListView):
    model = Type
    template_name = "prices.html"
#class PricesDatailView(DetailView):
    #model = Type
    #template_name = "detail.html"
class PricesDatailView(DetailView):
    model = Type
    template_name = "detail.html"
