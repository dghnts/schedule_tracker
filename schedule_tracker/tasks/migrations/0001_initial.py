# Generated by Django 5.2 on 2025-04-26 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='タスク名')),
                ('description', models.TextField(blank=True, max_length=200, verbose_name='説明（任意）')),
                ('due_date', models.DateField(verbose_name='期限')),
                ('status', models.CharField(choices=[('tido', '未着手'), ('doing', '進行中'), ('done', '完了')], default='todo', verbose_name='進捗状況')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日')),
            ],
        ),
    ]
