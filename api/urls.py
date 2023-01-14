from django.urls import path
from . import views

urlpatterns = [
    path('getfilme/', views.getfilme, name='getfilme')   
]