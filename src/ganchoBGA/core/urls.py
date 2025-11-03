from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('colecciones/', views.colecciones, name='colecciones'),
    path('contacto/', views.contacto, name='contacto'),
]
