from rest_framework import serializers
from .models import Agendamento

class AgendamentoSerializer(serializers.ModelSerializer):
    valor_pagamento = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Agendamento
        fields = '__all__'
