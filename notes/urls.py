from django.urls import path

from . import views

urlpatterns = [
    path('not3es/', views.list, name='list'),
    path('notes/<int:pk>', views.detail, name='detail'),
]
