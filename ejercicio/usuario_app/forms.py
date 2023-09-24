from datetime import date
from django import forms
from .models import Usuario

CIERTA_EDAD = 15

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

class UsuarioForm(forms.ModelForm):
    
    confirmar_password = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean_birthday(self):
        birthday = self.cleaned_data['birthday']
        edad = calculate_age(birthday)

        if birthday > date.today():
            raise forms.ValidationError(
                    f"Solo fechas en el pasado."
                )

        if edad < CIERTA_EDAD:
            raise forms.ValidationError(
                    f"La edad debe ser mayor o igual a {CIERTA_EDAD} años, tienes {edad} años."
                )
        return birthday

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if not nombre.strip():  # Verifica si el nombre está vacío después de eliminar espacios en blanco
            raise forms.ValidationError("El nombre no puede estar vacío")
        return nombre

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('password') != cleaned_data.get('confirmar_password'):
            raise forms.ValidationError(
                    "Las contraseñas no coinciden"
                )

    class Meta:
        model = Usuario
        fields  = ['nombre', 'apellido', 'username', 'email', 'birthday', 'peso', 'password']

        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'username': 'Nombre de Usuario',
            'email': 'Correo Electrónico',
            'birthday': 'Fecha de Nacimiento',
            'peso': 'Peso',
            'password': 'Contraseña',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'max': date.today().strftime('%Y-%m-%d')}),
            'peso': forms.NumberInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
