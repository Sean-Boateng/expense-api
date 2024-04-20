from django.urls import path, include
from budget import views

urlpatterns = [
    path('', views.user_budgets),
    path('all/', views.get_all_budgets),
    path('update/<int:pk>/', views.update_budgets),
]