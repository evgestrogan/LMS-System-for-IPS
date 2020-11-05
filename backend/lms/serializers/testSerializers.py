from rest_framework import serializers
from ..models import Test


class AnswerSerializer(serializers.Serializer):
    """
    Сериализатор для ответа на вопрос
    """
    id = serializers.IntegerField(required=False)
    body = serializers.CharField(required=False)
    choice = serializers.ChoiceField(choices=[True, False])


class QuestionSerializer(serializers.Serializer):
    """
    Сериализатор вопроса для теста
    """
    id = serializers.IntegerField(required=False)
    body = serializers.CharField(required=False)
    answer = AnswerSerializer(read_only=True, many=True)


class ResultTestSerializer(serializers.Serializer):
    """
    Сериализатор теста для курса и главы
    """
    id = serializers.IntegerField(required=False)
    title = serializers.CharField()
    question = QuestionSerializer(many=True)


class TestSerializer(serializers.Serializer):
    """
    Сериализатор теста для курса и главы
    """
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False)


class TestSerializerForCreate_Update(serializers.Serializer):
    id = serializers.CharField(required=False)
    title = serializers.CharField()

    def create(self, validated_data):
        return Test.objects.create(**validated_data)
