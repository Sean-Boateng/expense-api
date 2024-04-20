from django.urls import path, include
from envelope import views

urlpatterns = [
    path('<int:pk>/', views.user_envelopes),
    path('<int:pk>/add/', views.create_envelopes),
]