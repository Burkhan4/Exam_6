from django.urls import path
from . import views

urlpatterns = [
    path('', views.poet_list, name='poet_list'),
    path('create/', views.poet_create, name='poet_create'),
    path('edit/<int:pk>/', views.poet_edit, name='poet_edit'),
    path('delete/<int:pk>/', views.poet_delete, name='poet_delete'),
]
