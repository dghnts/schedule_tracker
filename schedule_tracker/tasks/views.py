from django.shortcuts import render

from django.views import View

# Create your views here.
class TaskIndexView(View):
    def get(self, request, *args):
        # タスク一覧ページを表示する
        return render(request,"tasks/index.html")

task_index_view = TaskIndexView.as_view()