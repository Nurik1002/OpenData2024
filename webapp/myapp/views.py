from .predict import load_image, predict
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Image
from django.http import Http404

def home(request):
    context = {}
    if request.method == "POST" and request.FILES.get("file"):
        uploaded_file = request.FILES["file"]
        obj = Image(image=uploaded_file) 
        obj.save()
        context["image_url"] = obj.image.url
        return redirect("result", img=obj.image.url)
    else:
        context["image_url"] = None
    return render(request, "index.html", context=context)



def result(request, img):
    try:
        image_obj = Image.objects.get(image=img)
    except Image.DoesNotExist:
        raise Http404("Image does not exist")
    
    return render(request, "result.html", {"image_obj": image_obj})
