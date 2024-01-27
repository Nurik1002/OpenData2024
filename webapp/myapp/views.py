from .predict import load_image, predict
from django.shortcuts import render

def home(request):
    return render(request, 'index.html', {})

def get_predict(request):
    context = {}
    if request.method=="POST":
        file = request.FILES
        context["file"] = file
        return render(request, 'result.html', context=context)
        

