from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Envelope
from .serializers import EnvelopeSerializer
from django.shortcuts import get_object_or_404

# Create your views here.
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def user_envelopes(request,pk):
#     print(
#         'User ', f"{request.user.id} {request.user.email} {request.user.username}")
#     if request.method == 'GET':
#         envelopes = Envelope.objects.filter(user_id=pk)
#         serializer = EnvelopeSerializer(envelopes, many=True)
#         return Response(serializer.data)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def user_envelopes(request):
    print('User ', f"{request.user.id}  {request.user.username}")
    envelopes = Envelope.objects.filter(user_id=request.user.id)

    if request.method == 'POST':
        serializer = EnvelopeSerializer(data=request.data)
        if serializer.is_valid():
            envelope = serializer.save(user=request.user)
            envelope.balance = envelope.amount  # Update balance based on amount
            envelope.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        serializer = EnvelopeSerializer(envelopes, many=True)
        return Response(serializer.data)


# @api_view([ 'POST'])
# @permission_classes([IsAuthenticated])
# def create_envelopes(request,pk):
#     print(
#         'User ', f"{request.user.id} {request.user.email} {request.user.username}")

#     serializer = EnvelopeSerializer(data=request.data)
#     if serializer.is_valid():
#         envelope = serializer.save(user=request.user)
#         envelope.balance = envelope.amount
#         # envelope.save()
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['PUT','DELETE'])
# def update_envelopes(request,pk,pk2):
#     try:
#         envelope = Envelope.objects.get(user=request.user,pk=pk)
#     except Envelope.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'PUT':
#         serializer = EnvelopeSerializer(envelope,data=request.data)
#         if serializer.is_valid():
#             envelope.save()
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         envelope.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def edit_envelopes(request, pk):
    envelope = get_object_or_404(Envelope, pk=pk)
    if request.method == 'PUT':
        serializer = EnvelopeSerializer(envelope, data=request.data)
        serializer.is_valid(raise_exception=True)
        envelope.balance = envelope.amount  # Update balance based on amount
        envelope.save()
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        envelope.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)