from django.urls import path, include
from expense import views

urlpatterns = [
    path('<int:pk>/', views.envelope_expenses),
    path('edit/<int:pk>/', views.edit_expenses)
]