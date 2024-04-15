from django.urls import path, include
from envelope import views

urlpatterns = [
    path('', views.user_envelopes),
    path('all/', views.get_all_envelopes),
    path('update/<int:pk>/', views.update_envelope),
]