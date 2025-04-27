from django.urls import path

app_name = 'schedules'
from .views import schedule_index_view, schedule_register_view, schedule_update_view, schedule_delete_view

urlpatterns = [
    path('', schedule_index_view,name='index'),
    path('register', schedule_register_view,name="register"),
    path('update/<int:pk>', schedule_update_view, name="update"),
    path('delete/<int:pk>', schedule_delete_view, name="delete")
    # TODO: スケジュール一覧へ遷移するためのルーティング
]
