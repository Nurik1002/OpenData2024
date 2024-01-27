from .predict import load_image, predict
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Image
from django import forms


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = "__all__"


def home(request):
    context = {}
    if request.method == 'POST':
       form = UploadFileForm(request.POST, request.FILES)
       if form.is_valid():
           img = form.changed_data.get("file")
           image = Image.objects.create(image=img)
           obj = image.save()
           
           return redirect("result", {"img":"image"})
    else:
        form = UploadFileForm()
    context["form"] = form
        
    return render(request, 'index.html', context)

from django.shortcuts import render

def result(request):
    return render(request, 'result.html',{})


        

