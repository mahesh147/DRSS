from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('update/<int:relief_center_id>/', views.update, name='update'),
    path('delete/<int:relief_center_id>/', views.delete, name='delete'),
    path('view/<int:relief_center_id>/', views.view, name='view'),
]
