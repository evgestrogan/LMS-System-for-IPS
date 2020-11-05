from django.contrib import admin
from .models import *


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    """Поля преподавателя для Django-Admin"""
    list_display = ('user', 'avatar', )


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """Поля студента для Django-Admin"""
    list_display = ('user', 'group', 'avatar', )


@admin.register(StudyGroup)
class StudyGroupAdmin(admin.ModelAdmin):
    """Поля группы для Django-Admin"""
    list_display = ('number', 'type', )


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    """Поля кафедры для Django-Admin"""
    list_display = ('name', 'manager', )


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    """Поля предмета для Django-Admin"""
    list_display = ('name', 'manager', 'department', )


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """Поля курса для Django-Admin"""
    list_display = ('name', 'manager', 'subject', 'test', 'get_amount_trainee', )


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    """Поля главы для Django-Admin"""
    list_display = ('number', 'name', 'course', 'test', )


@admin.register(Subchapter)
class SubchapterAdmin(admin.ModelAdmin):
    """Поля подглавы для Django-Admin"""
    list_display = ('number', 'name', 'body', 'chapter', )


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    """Поля теста для Django-Admin"""
    list_display = ('title', 'get_amount_user', )


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Поля ответа для Django-Admin"""
    list_display = ('body', 'test')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    """Поля ответа для Django-Admin"""
    list_display = ('body', 'question', 'choice',)
