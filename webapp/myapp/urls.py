from django.urls import path
from .views import home, result

urlpatterns = [
    path("result/", result , name="result"),
    path("", home, name="home"),    
]