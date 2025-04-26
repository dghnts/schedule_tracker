from datetime import datetime,date
from django.shortcuts import render,redirect
from django.db.models import Q

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
        # 優先順位の高いもの（期日が迫っているもの->進捗状況）の昇順にsort
        context["tasks"] = Task.objects.filter(Q(due_date__gte=datetime.now().date())|Q(status__regex="[01]")).order_by('due_date','status')
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
        # form二送信された値をコピー
        copy = request.POST.copy()

        # statusに初期値を設定する
        copy["status"] = "0"

        #formに送信されたデータを追加
        post_form = TaskRegisterForm(copy)

        # バリデーションエラーのチェック
        if not post_form.is_valid():
            print(post_form.errors)
            print("エラーがあります")
        else:
            # 問題なければformの内容を保存
            post_form.save()

        return redirect("tasks:index")

task_register_view = TaskRegisterView.as_view()

class TaskUpdateView(View):
    def get(self,request,pk,*args, **kwargs):
        # templateに渡す値（context）の用意
        context = dict()
        # idがpkであるタスクをtaskという名前でcontext二格納
        context["task"] = Task.objects.get(id=pk)

        return render(request, "tasks/update.html",context)

    def post(self,request, pk, *args, **kwargs):
        # pkをidにもつtaskの情報を取得
        task = Task.objects.get(id=pk)

        # 送信された情報でtaskの情報を更新する
        post_form = TaskRegisterForm(request.POST,instance=task)

        # バリデーションエラーのチェック
        if not post_form.is_valid():
            print("エラーがあります")
        else:
            # 問題なければformの内容を保存
            post_form.save()

        return redirect("tasks:index")


task_update_view = TaskUpdateView.as_view()