from django.urls import path
from todolist.views import show_todolist, create_task, register, login_user, logout_user, update_task, delete_task
from todolist.views import show_json, create_task_ajax, delete_task_ajax

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('create-task', create_task, name='create_task'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('update-task/<str:pk>', update_task, name='update_task'),
    path('delete-task/<str:pk>', delete_task, name='delete_task'),
    path('json/', show_json, name='show_json'),
    path('add/', create_task_ajax, name='create_task_ajax'),
    path('delete/<str:pk>', delete_task_ajax, name='delete_task_ajax'),
]