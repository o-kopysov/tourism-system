from django.shortcuts import render
from .models import Sight
from django.views.generic import ListView,DetailView

#def index(request):
    #sights = Sight.objects.all()
    #return render(request,'home.html', {'sights':sights})
class HomeView(ListView):
    model = Sight
    template_name = "home.html"
    
class SightDatailView(DetailView):
    model = Sight
    template_name = "sight_one.html"
