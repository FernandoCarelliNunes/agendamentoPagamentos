from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Agendamento
from .serializers import AgendamentoSerializer

@api_view(['POST'])
def criar_agendamento(request):
    serializer = AgendamentoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listar_agendamentos(request):
    agendamentos = Agendamento.objects.all()
    serializer = AgendamentoSerializer(agendamentos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def consultar_agendamento(request, id):
    try:
        agendamento = Agendamento.objects.get(id=id)
    except Agendamento.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = AgendamentoSerializer(agendamento)
    return Response(serializer.data)

@api_view(['DELETE'])
def deletar_agendamento(request, id):
    try:
        agendamento = Agendamento.objects.get(id=id)
    except Agendamento.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    agendamento.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
