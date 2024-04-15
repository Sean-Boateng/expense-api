from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Envelope
from .seriaizers import EnvelopeSerializer


# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_envelopes(request):
    envelope = Envelope.objects.all()
    serializer = EnvelopeSerializer(envelope, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_envelopes(request):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == 'POST':
        serializer = EnvelopeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        cars = Envelope.objects.filter(user_id=request.user.id)
        serializer = EnvelopeSerializer(cars, many=True)
        return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
def update_envelope(request, pk):
    try:
        envelope = Envelope.objects.get(user=request.user, pk=pk)
    except Envelope.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = EnvelopeSerializer(envelope, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
         envelope.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)