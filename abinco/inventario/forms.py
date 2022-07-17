from django.forms import ModelForm, HiddenInput
from .models import Producto

class FormularioProducto(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        self.fields['nombre'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Ej. Caño PVC'})
        self.fields['codigo'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Ej. EAN765765765'})
        self.fields['marca'].widget.attrs.update({'class': 'form-select', 'placeholder': 'Ej. Tigre'})
        self.fields['categoria'].widget.attrs.update({'class': 'form-select', 'placeholder': 'Ej. Caño'})
        self.fields['stock'].widget.attrs.update({'class': 'form-control'})
        self.fields['ubicacion'].widget.attrs.update({'class': 'form-select', 'placeholder': 'Ej. A1'})
        self.fields['descripcion'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Escribir una descripción...'})

    class Meta:
        model = Producto
        fields = ['nombre', 'codigo', 'marca', 'categoria', 'stock', 'ubicacion', 'descripcion']

