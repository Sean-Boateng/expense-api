from django.urls import path, include
from envelope import views

urlpatterns = [
    path('', views.user_envelopes),
    path('edit/<int:pk>/', views.edit_envelopes),
]