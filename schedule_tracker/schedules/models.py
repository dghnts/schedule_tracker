from django.db import models

#from tasks.models import Task

# Create your models here.
class Schedule(models.Model):
    title = models.CharField(verbose_name="スケジュール名",max_length=255)
    date = models.DateField(verbose_name="日付")
    time = models.TimeField(verbose_name="時間",blank=True)
    memo = models.TextField(verbose_name="メモ",blank=True)

    #task = models.OneToOneField(Task, verbose_name="タスクID", on_delete=models.CASCADE, related_name='schedule')

    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="更新日時", auto_now=True)

    def __str__(self):
        return self.title