from django.shortcuts import render,redirect
from django.views import View

from .models import Task
from .forms import TaskRegisterForm
# Create your views here.
class TaskIndexView(View):
    def get(self, request, *args, **kwargs):
        # templateに渡す値(context)の用意
        context = dict()
        # 登録されているタスク一覧を取得する
        # tasksという名前でcontextに登録
        context["tasks"] = Task.objects.all()
        # タスク一覧ページを表示する
        return render(request,"tasks/index.html",context)

task_index_view = TaskIndexView.as_view()

class TaskRegisterView(View):
    def get(self, request, *args, **kwargs):
        context = dict()
        # formという名前でTaskRegisterFormを追加
        context["form"] = TaskRegisterForm()

        return render(request,"tasks/register.html",context)

    def post(self, request, *args, **kwargs):
        #formに送信されたデータを追加
        post_form = TaskRegisterForm(request.POST)
        print(request)
        # バリデーションエラーのチェック
        if not post_form.is_valid():
            print("エラーがあります")
        else:
            post_form.save()

        return redirect("tasks:index")

task_register_view = TaskRegisterView.as_view()