from django.shortcuts import render
from .models import Expense
from .serializers import ExpenseSerializer
from envelope.models import Envelope
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
# Create your views here.
@api_view(['GET', 'POST'])  # Add POST method
@permission_classes([IsAuthenticated])
def envelope_expenses(request, pk):
    if request.method == 'GET':
        envelope = get_object_or_404(Envelope, pk=pk, user=request.user)
        expenses = Expense.objects.filter(envelope=envelope)
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        envelope = get_object_or_404(Envelope, pk=pk, user=request.user)
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(envelope=envelope)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT','DELETE'])
@permission_classes([IsAuthenticated])
def edit_expenses(request,pk):
    expense = get_object_or_404(Expense, pk=pk)
    
    if request.method == 'PUT':
        serializer = ExpenseSerializer(expense, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)