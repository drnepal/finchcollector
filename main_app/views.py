from django.shortcuts import render
from .models import Finchcollecotr



def home(request):
    return render(request, 'home.html')

# about route
def about(request):
    return render(request, 'about.html')

# index route for cats
def finchcollector_index(request):
    # just like we passed data to our templates in express
    # we pass data to our templates through our view functions
    # we can gather relations from SQL using our model methods
    cats = Finchcollecotor.objects.all()
    return render(request, 'finchcollector/index.html', { 'cats': cats })