from rest_framework import serializers

from .chapterSerializers import ChapterSerializer
from .testSerializers import TestSerializer
from .userSerializers import ManagerSerializer
from .userSerializers import StudentSerializerForCourse
from ..models import Course


class CourseSerializerForDepartmentPage(serializers.Serializer):
    """
    Сериализатор для расширения SubjectSerializer
    """
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, max_length=50)
    test = TestSerializer(read_only=True)
    manager = ManagerSerializer(read_only=True)
    trainee = StudentSerializerForCourse(many=True)


class CourseSerializer(serializers.Serializer):
    """
    Сериализатор для страницы курса с его главами и подглавами,а также тестами
    """
    id = serializers.CharField()
    subject = serializers.CharField()
    name = serializers.CharField(required=False, max_length=50)
    test_id = serializers.CharField()
    chapter = ChapterSerializer(read_only=True, many=True)


class CourseSerializerForCreate_Update(serializers.Serializer):
    name = serializers.CharField()
    test_id = serializers.CharField()
    subject_id = serializers.CharField()
    manager_id = serializers.CharField()

    def create(self, validated_data):
        return Course.objects.create(**validated_data)