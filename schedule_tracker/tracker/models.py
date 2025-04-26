from django.db import models
from django.db.models import CharField
from django.template.defaultfilters import length


# Create your models here.
class Task(models.Model):
    title = models.CharField(verbose_name="タスク名",max_length=50)
    descrption = models.TextField(varbose_name="タスク詳細",max_length=200)
    due_date = models.DateField(verbose_name="期限",)
    status = models.CharField(verbose_name="進捗状況")
    created_at = models.DateTimeField(verbose_name="作成日")
    updated_at = models.DateTimeField(verbose_name="更新日")
