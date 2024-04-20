from django.shortcuts import render
from budget.models import Budget
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Envelope
from budget.models import Budget
from .serializers import EnvelopeSerializer
from django.shortcuts import get_object_or_404

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_envelopes(request,pk):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == 'GET':
        envelopes = Envelope.objects.filter(budget_id=pk)
        serializer = EnvelopeSerializer(envelopes, many=True)
        return Response(serializer.data)



@api_view([ 'POST'])
@permission_classes([IsAuthenticated])
def create_envelopes(request,pk):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    budget = get_object_or_404(Budget, id=pk)

    serializer = EnvelopeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.validated_data['budget'] = budget
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

