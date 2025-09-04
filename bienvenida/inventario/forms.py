from django import forms 
from .models import Producto

class ProductoForm(forms.ModelForm):
    class meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion', 'stock']