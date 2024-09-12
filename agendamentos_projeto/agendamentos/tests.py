from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Agendamento

class AgendamentoTests(APITestCase):

    def test_criar_agendamento(self):
        url = reverse('criar_agendamento')
        data = {
            "data_pagamento": "2024-09-15",
            "permite_recorrencia": True,
            "quantidade_recorrencia": 5,
            "intervalo_recorrencia": 30,
            "status_recorrencia": "Ativa",
            "agencia": 1234,
            "conta": 567890,
            "valor_pagamento": 1500.75
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_listar_agendamentos(self):
        # Cria um agendamento antes de testar
        Agendamento.objects.create(
            data_pagamento="2024-09-15",
            permite_recorrencia=True,
            quantidade_recorrencia=5,
            intervalo_recorrencia=30,
            status_recorrencia="Ativa",
            agencia=1234,
            conta=567890,
            valor_pagamento=150075
        )
        url = reverse('listar_agendamentos')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Espera que haja 1 agendamento

    def test_consultar_agendamento(self):
        # Cria um agendamento antes de testar
        agendamento = Agendamento.objects.create(
            data_pagamento="2024-09-15",
            permite_recorrencia=True,
            quantidade_recorrencia=5,
            intervalo_recorrencia=30,
            status_recorrencia="Ativa",
            agencia=1234,
            conta=567890,
            valor_pagamento=150075
        )
        url = reverse('consultar_agendamento', args=[agendamento.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], agendamento.id)

    def test_deletar_agendamento(self):
        # Cria um agendamento antes de testar
        agendamento = Agendamento.objects.create(
            data_pagamento="2024-09-15",
            permite_recorrencia=True,
            quantidade_recorrencia=5,
            intervalo_recorrencia=30,
            status_recorrencia="Ativa",
            agencia=1234,
            conta=567890,
            valor_pagamento=150075
        )
        url = reverse('deletar_agendamento', args=[agendamento.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
