from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizzamenu
# Create your views here.
def index(request):
 pizzamenu = Pizzamenu.objects.all()
 return render(request, 'index.html', {'pizzamenu':pizzamenu})

def about(request):
 return HttpResponse("<h1>About Page</h1>")



