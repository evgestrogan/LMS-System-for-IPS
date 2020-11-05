from rest_framework import serializers
from .userSerializers import ManagerSerializer
from .subjectSerializers import SubjectSerializer


class DepartmentSerializer(serializers.Serializer):
    """
    Сериализатор для получения кафедры со связанными с ней
    предметов и курсов
    """
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, max_length=25)
    subject = SubjectSerializer(read_only=True, many=True)
    manager = ManagerSerializer(read_only=True)


class DepartmentSerializerForSideBar(serializers.Serializer):
    """
    Сериализатор списка кафедр и их начальников для SideBar
    """
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, max_length=25)
    manager = ManagerSerializer(read_only=True)


