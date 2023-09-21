from django.urls import path     
from . import views

#los url parten de lo que este en urls.py de mi modulo principal (ejercicios)
urlpatterns = [
    path('', views.agregar_usuario),
    # path('formulario', views.some_function)

]