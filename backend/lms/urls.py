from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import DepartmentList, DepartmentDetail, UserDetail, ProfileDetail, CourseDetail, SubchapterDetail, TestDetail, CourseList, TestList, ChapterList

app_name = 'api'

urlpatterns = [
    path('user/<int:pk>/', UserDetail.as_view()),
    path('profile/<int:pk>/', ProfileDetail.as_view()),
    path('departments/', DepartmentList.as_view()),
    path('department/<int:pk>/', DepartmentDetail.as_view()),
    path('courses/', CourseList.as_view()),
    path('course/<int:pk>/', CourseDetail.as_view()),
    path('chapter/', ChapterList.as_view()),
    path('subchapter/<int:pk>/', SubchapterDetail.as_view()),
    path('subchapter/', SubchapterDetail.as_view()),
    path('tests/', TestList.as_view()),
    path('test/<int:pk>/', TestDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
