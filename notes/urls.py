from django.urls import path

from . import views

urlpatterns = [
    path('notes/', views.list, name='list'),
    path('notes/<int:pk>', views.detail, name='detail'),
]
