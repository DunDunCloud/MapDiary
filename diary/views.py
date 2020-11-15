from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Place

# Create your views here.
def index(request):
    # place = get_object_or_404(Place, name='place')
    return render(request, 'index.html')
