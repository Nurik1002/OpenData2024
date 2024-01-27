#from ...predict import load_image, predict
from django.shortcuts import render

def home(request):
    return render(request, 'index.html', {})