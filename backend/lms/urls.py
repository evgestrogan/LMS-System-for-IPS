from django.urls import path, re_path
from rest_framework.routers import DefaultRouter

from .views import DepartmentViewSet, CourseViewSet, SubjectViewSet, ChapterViewSet, SubchapterViewSet, \
    User_infoViewSet, QuestionViewSet, ChapterSimpleViewSet

app_name = 'api'

router = DefaultRouter()
router.register('departments', DepartmentViewSet, basename='departments')
router.register('courses', CourseViewSet, basename='courses')
router.register('subjects', SubjectViewSet, basename='subject')
router.register('chapters', ChapterViewSet, basename='Chapter')
router.register('chaptersSimple', ChapterSimpleViewSet, basename='ChapterSimple')
router.register('subchapters', SubchapterViewSet, basename='Subchapter')
router.register('user_info', User_infoViewSet, basename='Subchapter')
router.register('question', QuestionViewSet, basename='Answer')
urlpatterns = router.urls
