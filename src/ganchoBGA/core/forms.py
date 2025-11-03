from django import forms
from .models import Bolso


class BolsoForm(forms.ModelForm):
    """
    Formulario para crear y editar bolsos
    """
    class Meta:
        model = Bolso
        fields = ['product_display_name', 'base_colour', 'local_image']
        widgets = {
            'product_display_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del bolso'
            }),
            'base_colour': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Color del bolso'
            }),
            'local_image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            })
        }
        labels = {
            'product_display_name': 'Nombre del Producto',
            'base_colour': 'Color Base',
            'local_image': 'Imagen del Bolso'
        }
