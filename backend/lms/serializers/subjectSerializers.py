from rest_framework import serializers

from .courseSerializers import CourseSerializerForDepartmentPage
from .userSerializers import ManagerSerializer


class SubjectSerializer(serializers.Serializer):
    """
    Сериализатор для расширения DepartmentSerializer
    """
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, max_length=50)
    manager = ManagerSerializer(read_only=True)
    course = CourseSerializerForDepartmentPage(read_only=True, many=True)