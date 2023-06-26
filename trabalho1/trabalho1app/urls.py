from django.urls import path
from .views import index, aluno, contato


urlpatterns = [path("",index,name='index'), 
               path('aluno/<int:id>', aluno, name='aluno'),
               path('contato/', contato, name='contato'),
               ]



