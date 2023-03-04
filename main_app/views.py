from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch

# temporary finchs for building templates
# finchs = [
#     {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
#     {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
#     {'name': 'Tubs', 'breed': 'ragdoll', 'description': 'chunky lil guy', 'age': 0},
# ]

# Create your views here.
# view functions match urls to code (like controllers in Express)
# define our home view function
def home(request):
    return render(request, 'home.html')

# about route
def about(request):
    return render(request, 'about.html')

# index route for finchs
def finchs_index(request):
    # just like we passed data to our templates in express
    # we pass data to our templates through our view functions
    # we can gather relations from SQL using our model methods
    finchs = Finch.objects.all()
    return render(request, 'finchs/index.html', { 'finchs': finchs })

# detail route for finchs
# finch_id is defined, expecting an integer, in our url
def finchs_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)

    return render(request, 'finchs/detail.html', { 'finch': finch })

class FinchCreate(CreateView):
    model = Finch
    # the fields attribute is required for a createview. These inform the form
    fields = '__all__'
    # we could also have written our fields like this:
    # fields = ['name', 'breed', 'description', 'age']
    # we need to add redirects when we make a success
    # success_url = '/finchs/{finch_id}'
    # or, we could redirect to the index page if we want
    # success_url = '/finchs'
    # what django recommends, is adding a get_absolute_url method to the model

class FinchUpdate(UpdateView):
    model = Finch
    # let's use custom fields to disallow renaming a finch
    fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finchs/'