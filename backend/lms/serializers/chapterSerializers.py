from rest_framework import serializers

from .subchapterSerializers import SubchapterSerializer
from .testSerializers import TestSerializer


class ChapterSerializer(serializers.Serializer):
    """
    Сериализатор для расширения CourseSerializer
    """
    id = serializers.IntegerField(read_only=True)
    number = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, max_length=150)
    test = TestSerializer(read_only=True)
    subchapter = SubchapterSerializer(read_only=True, many=True)