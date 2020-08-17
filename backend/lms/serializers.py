from rest_framework.serializers import ModelSerializer
from .models import Department, Course, Subject


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ['subject', 'name_course']
        depth = 2


class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = ['department', 'name_subject']


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = ['name_department',]
