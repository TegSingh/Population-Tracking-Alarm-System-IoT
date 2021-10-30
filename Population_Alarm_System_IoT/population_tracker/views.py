from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Sensor_data
from django.http import Http404

# Create your views here.

# Home page to show the number of people entering [list view]
def home(request):
    try:
        sensor_data = Sensor_data.objects.all()
        population = Sensor_data.objects.all().count()
    except:
        raise Http404()

    context = {"population" : population, "Sensor_data" : sensor_data}

    return render(request, "population_tracker/home.html", context)

# Method to add random data for testing purposes 
def util_add_random_sensor_data(): 
    pass

# Method to delete data
def sensor_data_delete(): 
    pass

# Method to show data for a particulat date
def display_date_filtered_data():
    pass

# Method to show data for a particulat hour
def display_hour_filtered_data():
    pass

# Method to calculate total number of people
def calculate_total_objects(): 
    pass
