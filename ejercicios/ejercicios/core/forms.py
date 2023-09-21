from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['full_name', 'age', 'weight', 'image']

        labels = {
            'full_name': 'Nombre Completo',
            'age': 'Edad',
            'weight': 'Peso',
            'image': 'Imagen de Perfil',
        }

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

