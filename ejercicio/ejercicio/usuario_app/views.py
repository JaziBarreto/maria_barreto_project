from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            # Puedes agregar aquí cualquier lógica adicional, como iniciar sesión automáticamente al usuario
            return redirect('login')  # Redirige al usuario a la página de inicio de sesión
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

# def index(request):
#     return render (request, "index.html")

# def one_method(request):                # no se pasan valores a través de URL
#     pass                                
    
# def another_method(request, my_val):	# my_val sería un número de la URL
#     pass                                # dado el ejemplo anterior, my_val sería 23
    
# def yet_another(request, name):	        # el nombre sería una cadena de la URL
#     pass                                # dado el ejemplo anterior, el nombre sería 'pooh'
    
# def one_more(request, id, color): 	# id sería un número y colorea una cadena de la URL
#     pass                                # dado el ejemplo anterior, la identificación sería 17 y color sería 'brown'
