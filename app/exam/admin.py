from django.contrib import admin
from exam import models

# Register your models here.


@admin.register(models.Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")


@admin.register(models.Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ("id", "exam", "question")


@admin.register(models.AnswerOptions)
class AnswerOptionsAdmin(admin.ModelAdmin):
    list_display = ("id", "options", "question", "id")
