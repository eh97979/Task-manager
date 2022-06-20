from django.contrib import admin
from django.urls import path 

from . import views

app_name = 'task'


urlpatterns=[
    # path('', views.index, name='index')
    path('', views.TasksView.as_view(), name='index'),
    path('addtask/', views.add_task, name='addtask'),
    path('remover/', views.remove_all_task, name='rm_task'),
    path('rm/<int:task_pk>', views.remove_1_task, name='rm')
]
