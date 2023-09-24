from django.urls import path     
from . import views #means that views is in the same directory as this

urlpatterns = [
    #path('', views.index, name='index')
    path('', views.register, name='register'),
]
urlpatterns = [

#     path('bears', views.one_method),                        # solo coincidiría con localhost:8000/bears
#     path('bears/<int:my_val>', views.another_method),       # solo coincidiría con localhost:8000/bears/23
#     path('bears/<str:poke>/poke', views.yet_another),       # solo coincidiría con localhost:8000/bears/pooh/poke
#     path('<int:id>/<str:color>', views.one_more),           # solo coincidiría con localhost:8000/17/brown
]
