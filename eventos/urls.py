
from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('evento/<int:evento_id>/', views.detalhe_evento, name='detalhe_evento'),
    path('evento/novo/', views.criar_evento, name='criar_evento'),
    path('evento/<int:evento_id>/editar/', views.editar_evento, name='editar_evento'),
    path('evento/<int:evento_id>/excluir/', views.excluir_evento, name='excluir_evento'),
]
