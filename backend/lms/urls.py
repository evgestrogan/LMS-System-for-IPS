from rest_framework.routers import DefaultRouter

from .views import DepartmentViewSet, CourseViewSet, SubjectViewSet, ChapterViewSet

app_name = 'api'

router = DefaultRouter()
router.register('departments', DepartmentViewSet, basename='departments')
router.register('courses', CourseViewSet, basename='courses')
router.register('subjects', SubjectViewSet, basename='subject')
router.register('chapters', ChapterViewSet, basename='Chapter')

urlpatterns = router.urls