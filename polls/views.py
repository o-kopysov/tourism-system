from django.shortcuts import render
from .models import Sight
def index(request):
    sights = Sight.objects.all()
    return render(request,'home.html', {'sights':sights})
