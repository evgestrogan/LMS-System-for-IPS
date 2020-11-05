from rest_framework import serializers


class SubchapterSerializer(serializers.Serializer):
    """
    Сериализатор для расширения ChapterSerializer
    """
    id = serializers.IntegerField(read_only=True)
    number = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, max_length=150)
    body = serializers.FileField()