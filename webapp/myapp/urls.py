from django.urls import path
from .views import home, get_predict

urlpatterns = [
    path("result/", get_predict, name="result"),
    path("", home, name="home"),    
]