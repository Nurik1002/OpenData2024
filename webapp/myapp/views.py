from .predict import load_image, predict
from django.shortcuts import render
from django.shortcuts import redirect
from PIL import Image as IMG
from .models import Image
from django.http import Http404
from django.conf import settings
import os


def home(request):
    context = {}
    if request.method == "POST" and request.FILES.get("file"):
        uploaded_file = request.FILES["file"]
        obj = Image(image=uploaded_file) 
        obj.save()
        context["image_url"] = obj.image.url
        return redirect("result", pk=obj.id)

    else:
        context["image_url"] = None
    return render(request, "index.html", context=context)



def result(request, pk):
    context = {}
    try:
        image_obj = Image.objects.get(id=pk)
        context["image_obj"] = image_obj
        img = load_image(os.path.join(settings.BASE_DIR, image_obj.image.path))
        pred = predict(img)
        context["predict"] = pred

    except Image.DoesNotExist:
        raise Http404("Image does not exist")
    
    return render(request, "result.html", context)
