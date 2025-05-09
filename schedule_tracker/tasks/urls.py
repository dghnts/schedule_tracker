"""
URL configuration for schedule_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

app_name = 'tasks'
from .views import task_index_view, task_register_view, task_update_view, task_delete_view

urlpatterns = [
    path('', task_index_view,name='index'),
    path('register', task_register_view,name="register"),
    path('update/<int:pk>', task_update_view, name="update"),
    path('delete/<int:pk>', task_delete_view, name="delete")
    # TODO: スケジュール一覧へ遷移するためのルーティング
]
