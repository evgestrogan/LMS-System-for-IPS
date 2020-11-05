from rest_framework import serializers


class StudentSerializerForCourse(serializers.Serializer):
    id = serializers.CharField()
    user_id = serializers.CharField()
    group = serializers.CharField()


class StudentSerializerForUser(serializers.Serializer):
    """
    Сериализатор для студента для API user
    """
    avatar = serializers.ImageField()
    group = serializers.CharField(required=False, max_length=5)


class ManagerSerializerForUser(serializers.Serializer):
    """
    Сериализатор перподавателя для API user
    """
    id = serializers.CharField()
    avatar = serializers.ImageField()


class UserSerializerForManager_Student(serializers.Serializer):
    """
    Сериализатор пользователя, для расширения данных
    в сериализаторах "Manager"
    """
    id = serializers.IntegerField(read_only=True)
    last_name = serializers.CharField(required=False, max_length=25)
    first_name = serializers.CharField(required=False, max_length=25)
    second_name = serializers.CharField(required=False, max_length=25)


class UserSerializer(serializers.Serializer):
    """
    Сериализатор пользователя, API user
    """
    id = serializers.IntegerField(read_only=True)
    last_name = serializers.CharField(required=False, max_length=25)
    first_name = serializers.CharField(required=False, max_length=25)
    second_name = serializers.CharField(required=False, max_length=25)
    manager = ManagerSerializerForUser(read_only=True)
    student = StudentSerializerForUser(read_only=True)


class ManagerSerializer(serializers.Serializer):
    """
    Сериализатор перподавателя для DepartmentSerializerForSideBar
    """
    user = UserSerializerForManager_Student(read_only=True)
    avatar = serializers.ImageField()

