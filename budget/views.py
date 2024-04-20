from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Budget
from .serializers import BudgetSerializer


# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_budgets(request):
    budget = Budget.objects.all()
    serializer = BudgetSerializer(budget, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_budgets(request):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == 'POST':
        serializer = BudgetSerializer(data=request.data)
        
        if serializer.is_valid():
            budget = serializer.save(user=request.user)
            budget.balance = budget.amount  # Calculate balance
            budget.save()  # Save the updated budget with balance
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        budget = Budget.objects.filter(user_id=request.user.id)
        serializer = BudgetSerializer(budget, many=True)
        return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
def update_budgets(request, pk):
    try:
       budget = Budget.objects.get(user=request.user, pk=pk)
    except Budget.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = BudgetSerializer(budget, data=request.data)
        if serializer.is_valid():
            budget.balance = budget.amount  # Calculate balance
            budget.save() 
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
         budget.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)