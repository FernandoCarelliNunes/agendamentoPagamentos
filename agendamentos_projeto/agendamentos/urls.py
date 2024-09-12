from django.urls import path
from . import views

urlpatterns = [
    path('api/agendamentos/', views.criar_agendamento, name='criar_agendamento'),
    path('api/agendamentos/', views.listar_agendamentos, name='listar_agendamentos'),
    path('api/agendamentos/<int:id>/', views.consultar_agendamento, name='consultar_agendamento'),
    path('api/agendamentos/<int:id>/', views.deletar_agendamento, name='deletar_agendamento'),
]
