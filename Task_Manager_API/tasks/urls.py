from django.urls import path 
from . import views

urlpatterns = [
    path('tasks/', views.TaskListCreateAPIView.as_view()),
    path('tasks/<int:id>/', views.TaskDetailAPIView.as_view()),
    path('categories/', views.CategoryListCreateAPIView.as_view())
]