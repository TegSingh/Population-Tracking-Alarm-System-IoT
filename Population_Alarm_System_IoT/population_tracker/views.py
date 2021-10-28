from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here.

# Home page to show the number of people entering
def home(request):
    context = {"population" : 39}
    return render(request, "population_tracker/home.html", context)