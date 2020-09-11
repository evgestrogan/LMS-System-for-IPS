from rest_framework.serializers import ModelSerializer
from .models import Department, Course, Subject, Chapter, Subchapter


class SubchapterSerializer(ModelSerializer):
    class Meta:
        model = Subchapter
        fields = '__all__'


class ChapterSerializer(ModelSerializer):
    subchapters = SubchapterSerializer(many=True, read_only=True)
    class Meta:
        model = Chapter
        depth = 1
        fields = ['id', 'course', 'name_chapter', 'test', 'subchapters']


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class SubjectSerializer(ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)
    class Meta:
        model = Subject
        depth = 1
        fields = ['name_subject', 'courses']


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = ['name_department']
