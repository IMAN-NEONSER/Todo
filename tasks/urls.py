from django.urls import path
from . import views



app_name = 'tasks'
urlpatterns = [
    path('add_task/', views.AddTaskView.as_view()),
]