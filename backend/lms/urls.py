from rest_framework.routers import DefaultRouter

from .views import DepartmentViewSet, CourseViewSet

app_name = 'api'

router = DefaultRouter()
router.register('departments', DepartmentViewSet, basename='departments')
router.register('courses', CourseViewSet, basename='courses')

urlpatterns = router.urls