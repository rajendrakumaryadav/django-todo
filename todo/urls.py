from django.urls import path

from . import views

urlpatterns = [
    path('', views.todoView, name='todo'),
    path('addTodo/', views.addTodo, name='add_todo'),
    path('deleteTodo/<int:todo_id>/', views.deleteTodo, name='delete_todo'),
]
