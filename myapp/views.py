from django.shortcuts import render
from .models import Products

# Create your views here.
def categories(request):
    return {
        'categories': Category.objects.all()
    }
def index(request):
    """ A view to return the index page """

    return render(request, 'myapp/index.html')
