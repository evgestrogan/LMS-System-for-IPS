
from rest_framework.serializers import ModelSerializer
from .models import Department, Course, Subject, Chapter, Subchapter, User_info, Question, Answer, Test


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class QuestionSerializer(ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        depth = 2
        fields = ['id', 'body', 'test', 'answer']


class SubchapterSerializer(ModelSerializer):
    class Meta:
        model = Subchapter
        fields = '__all__'


class SubchapterSimpleSerializer(ModelSerializer):
    class Meta:
        model = Subchapter
        fields = ['id', 'name_subchapter', 'body']


class ChapterSerializer(ModelSerializer):
    subchapters = SubchapterSimpleSerializer(many=True, read_only=True)
    class Meta:
        model = Chapter
        depth = 1
        fields = ['id', 'course', 'name_chapter', 'test', 'subchapters']


class ChapterSimpleSerializer(ModelSerializer):
    subchapters = SubchapterSimpleSerializer(many=True, read_only=True)
    class Meta:
        model = Chapter
        depth = 2
        fields = ['id', 'name_chapter', 'test', 'subchapters']


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        depth = 1
        fields = ['id', 'name_course', 'boss_course', 'test', 'user']


class CourseSimpleSerializer(ModelSerializer):
    class Meta:
        model = Course
        depth = 1
        fields = ['id', 'name_course', 'subject']


class SubjectSerializer(ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)
    class Meta:
        model = Subject
        depth = 1
        fields = ['id', 'name_subject', 'boss_subject', 'courses']


class SubjectSimpleSerializer(ModelSerializer):
    class Meta:
        model = Subject
        depth = 1
        fields = ['id', 'name_subject', 'department']



class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class DepartmentSimpleSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name_department']


class User_infoSerializer(ModelSerializer):
    boss_department = DepartmentSimpleSerializer(read_only=True)
    boss_subject = SubjectSimpleSerializer(read_only=True)
    boss_course = CourseSimpleSerializer(many=True, read_only=True)
    class Meta:
        model = User_info
        depth = 2
        fields = ['boss_department', 'boss_subject', 'boss_course', 'id', 'first_name', 'last_name', 'second_name', 'user_id', 'avatar', 'group_id']
