from rest_framework import serializers


class DepartmentSerializer(serializers.Serializer):
    """
    Сериализатор кафедры для API profile
    """
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, max_length=25)


class DepartmentSerializerForSubject(serializers.Serializer):
    """
    Сериализатор кафедры для сериализатора предмета
    """
    id = serializers.IntegerField(read_only=True)


class SubjectSerializer(serializers.Serializer):
    """
    Сериализатор предмета для API profile
    """
    id = serializers.IntegerField(read_only=True)
    department = DepartmentSerializerForSubject(read_only=True)
    name = serializers.CharField(required=False, max_length=50)


class SubjectSerializerForCourse(serializers.Serializer):
    """
    Сериализатор предмета для сериализатора курса
    """
    id = serializers.IntegerField(read_only=True)
    department = DepartmentSerializerForSubject(read_only=True)


class CourseSerializer(serializers.Serializer):
    """
    Сериализатор курса для API profile
    """
    id = serializers.IntegerField(read_only=True)
    subject = SubjectSerializerForCourse(read_only=True)
    name = serializers.CharField(required=False, max_length=50)


class ManagerSerializer(serializers.Serializer):
    """
    Сериализатор преподавателя для API profile
    """
    avatar = serializers.ImageField()
    department_manager = DepartmentSerializer(read_only=True, many=True)
    subject_manager = SubjectSerializer(read_only=True, many=True)
    course_manager = CourseSerializer(read_only=True, many=True)


class StudentSerializer(serializers.Serializer):
    """
    Сериализатор для студента для API profile
    """
    avatar = serializers.ImageField()
    group = serializers.CharField(required=False, max_length=5)
    course = CourseSerializer(many=True, read_only=True)


class UserSerializerForProfile(serializers.Serializer):
    """
    Сериализатор пользователя, API profile
    """
    id = serializers.IntegerField(read_only=True)
    # username = serializers.CharField(required=False, max_length=25)
    last_name = serializers.CharField(required=False, max_length=25)
    first_name = serializers.CharField(required=False, max_length=25)
    second_name = serializers.CharField(required=False, max_length=25)
    student = StudentSerializer(read_only=True)
    manager = ManagerSerializer(read_only=True)
