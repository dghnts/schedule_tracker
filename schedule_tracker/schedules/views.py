from contextlib import nullcontext
from datetime import datetime,time
from django.shortcuts import render,redirect
from django.db.models import Q

from django.views import View

from tasks.models import Task
from .models import Schedules
from .forms import ScheduleRegisterForm

# Create your views here.
class ScheduleIndexView(View):
    def get(self, request, *args, **kwargs):
        # templateに渡す値(context)の用意
        context = dict()
        # 登録されているタスク一覧を取得する
        # schedulesという名前でcontextに登録
        # 優先順位の高いもの（期日が迫っているもの->進捗状況）の昇順にsort
        context["schedules"] = Schedules.objects.all()
        # タスク一覧ページを表示する
        return render(request,"schedules/index.html",context)

schedule_index_view = ScheduleIndexView.as_view()

class ScheduleRegisterView(View):
    def get(self, request, *args, **kwargs):
        context = dict()
        # formという名前でScheduleRegisterFormを追加
        context["form"] = ScheduleRegisterForm()

        # 登録されているタスク一覧をcontext二格納
        context["tasks"] = Task.objects.filter(Q(due_date__gte=datetime.now().date())|Q(status__regex="[01]"))

        return render(request,"schedules/register.html",context)

    def post(self, request, *args, **kwargs):
        # 送信されたデータをコピー
        copy = request.POST.copy()

        if(not copy["time"]):
            copy["time"] = time(0,0)

        #formに送信されたデータを追加
        post_form = ScheduleRegisterForm(copy)

        # バリデーションエラーのチェック
        if not post_form.is_valid():
            print(post_form.errors)
            print("エラーがあります")
        else:
            # 問題なければformの内容を保存
            post_form.save()

        return redirect("schedules:index")

schedule_register_view = ScheduleRegisterView.as_view()

class ScheduleUpdateView(View):
    def get(self,request,pk,*args, **kwargs):
        # templateに渡す値（context）の用意
        context = dict()
        # idがpkであるタスクをscheduleという名前でcontext二格納
        context["schedule"] = Schedules.objects.get(id=pk)

        return render(request, "schedules/update.html",context)

    def post(self,request, pk, *args, **kwargs):
        # pkをidにもつscheduleの情報を取得
        schedule = Schedules.objects.filter(id=pk).first()

        # 送信された情報でscheduleの情報を更新する
        post_form = ScheduleRegisterForm(request.POST,instance=schedule)

        # バリデーションエラーのチェック
        if not post_form.is_valid():
            print("エラーがあります")
        else:
            # 問題なければformの内容を保存
            post_form.save()

        return redirect("schedules:index")

schedule_update_view = ScheduleUpdateView.as_view()

class ScheduleDeleteView(View):
    def get(self,request, pk,*args, **kwargs):
        context = dict()
        context["schedule"] = Schedules.objects.filter(id=pk).first()

        return render(request,"schedules/delete.html",context)

    def post(self,request, pk, *args, **kwargs):
        schedule = Schedules.objects.filter(id=pk).first()

        schedule.delete()

        return redirect("schedules:index")

schedule_delete_view = ScheduleDeleteView.as_view()
