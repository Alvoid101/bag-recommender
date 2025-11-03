from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('colecciones/', views.colecciones, name='colecciones'),
    path('contacto/', views.contacto, name='contacto'),
    path('agregar-bolso/', views.agregar_bolso, name='agregar_bolso'),
    path('editar-bolso/<int:bolso_id>/', views.editar_bolso, name='editar_bolso'),
    path('eliminar-bolso/<int:bolso_id>/', views.eliminar_bolso, name='eliminar_bolso'),
]
