from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    peso = forms.DecimalField(max_digits=5, decimal_places=2, required=False)
    foto_perfil = forms.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('peso', 'foto_perfil')
