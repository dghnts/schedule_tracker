from django.db import models
from django.db.models import CharField
from django.template.defaultfilters import length


# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ("0", "todo"),
        ("1", "doing"),
        ("2", "done")
    ]
    title = models.CharField(verbose_name="タスク名",max_length=50)
    description = models.TextField(verbose_name="説明（任意）",max_length=200,blank=True)
    due_date = models.DateField(verbose_name="期限",)
    status = models.CharField(verbose_name="進捗状況", choices=STATUS_CHOICES, default='0')
    created_at = models.DateTimeField(verbose_name="作成日",auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="更新日", auto_now=True)

    def __str__(self):
        return self.title
