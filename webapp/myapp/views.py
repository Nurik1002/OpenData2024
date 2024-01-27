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
    if request.method == 'POST':
       
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('result',  {"file":form})  
    else:
        
    return render(request, 'index.html', {'form': form})

from django.shortcuts import render

def result(request):
    return render(request, 'result.html',{})


        

