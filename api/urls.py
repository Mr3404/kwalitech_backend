from django.urls import path
from .task_tracker import views


urlpatterns = [
    path('requests/', views.RequestListAPIView.as_view(), name='request-list'),
    path('dashboard/', views.DashBoardView.as_view(), name='dashboard'),
    path('request/<int:pk>/', views.RequestView.as_view(), name='request-detail'),
    path('tasks/', views.TaskListView.as_view(), name='task-list'),
    path('task/<int:pk>/', views.TaskView.as_view(), name='task-detail'),
]
