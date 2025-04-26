from django.shortcuts import render
from django.views import View

from .models import Task

# Create your views here.
class TaskIndexView(View):
    def get(self, request, *args):
        # templateに渡す値(context)の用意
        context = dict()
        # 登録されているタスク一覧を取得する
        # tasksという名前でcontextに登録
        context["tasks"] = Task.objects.all()
        # タスク一覧ページを表示する
        return render(request,"tasks/index.html",context)

task_index_view = TaskIndexView.as_view()