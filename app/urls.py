from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.Task_list.as_view(), name='tasks'),
    path('tasks/<int:pk>/', views.TaskDetail.as_view(), name='task'),
    path('tasks/create/', views.TaskCreate.as_view(), name='task-create'),
    path('tasks/update/<int:pk>/', views.TaskUpdate.as_view(), name='task-update'),
    path('tasks/delete/<int:pk>/', views.TaskDelete.as_view(), name='task-delete'),

]
