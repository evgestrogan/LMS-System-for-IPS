from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework_simplejwt import authentication

from .models import Department, User, Course, Subchapter, Test, Question, Answer, Chapter, Student
from .serializers.departmentSerializers import DepartmentSerializerForSideBar, DepartmentSerializer
from .serializers.userSerializers import UserSerializer
from .serializers.profileSerializers import UserSerializerForProfile
from .serializers.courseSerializers import CourseSerializer
from .serializers.subchapterSerializers import SubchapterSerializer
from .serializers.testSerializers import ResultTestSerializer


class UserDetail(APIView):
    """
    Обработчик запросов для отдельного менеджера
    """
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JWTTokenUserAuthentication, ]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class ProfileDetail(APIView):
    """
    Обработчик запросов для отдельного пользователя
    """
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JWTTokenUserAuthentication, ]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializerForProfile(user)
        return Response(serializer.data)


class DepartmentList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JWTTokenUserAuthentication, ]

    def get(self, request, format=None):
        department = Department.objects.all()
        serializer = DepartmentSerializerForSideBar(department, many=True)
        return Response(serializer.data)


class DepartmentDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JWTTokenUserAuthentication, ]

    def get_object(self, pk):
        try:
            return Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        department = self.get_object(pk)
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)


class CourseList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JWTTokenUserAuthentication, ]

    def post(self, request, format=None):
        course_queryset = request.data
        try:
            Course.objects.filter(id=course_queryset['id']).update(name=course_queryset['name'])
            course = Course.objects.get(name=course_queryset['name'])
        except:
            course = Course.objects.create(subject_id=course_queryset['subject_id'],
                                           name=course_queryset['name'],
                                           manager_id=course_queryset['manager_id'],
                                           test_id=course_queryset['test_id'])
        return Response({'course_id': course.id}, status=status.HTTP_200_OK)


class CourseDetail(APIView):
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JWTTokenUserAuthentication, ]

    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        department = self.get_object(pk)
        serializer = CourseSerializer(department)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        student = Student.objects.get(user_id=request.data['user_id'])
        course = Course.objects.get(id=request.data['id'])
        course.trainee.add(student)
        return Response({'': ''}, status=status.HTTP_200_OK)


class ChapterList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JWTTokenUserAuthentication, ]

    def post(self, request, format=None):
        chapter_queryset = request.data
        try:
            Chapter.objects.filter(id=chapter_queryset['id']).update(number=chapter_queryset['number'],
                                                                     name=chapter_queryset['name'],
                                                                     test_id=chapter_queryset['test_id'])
            chapter = Chapter.objects.get(id=chapter_queryset['id'])
        except:
            chapter = Chapter.objects.create(course_id=chapter_queryset['id_course'],
                                             number=chapter_queryset['number'],
                                             name=chapter_queryset['name'],
                                             test_id=chapter_queryset['test_id'])
        return Response({'chapter_id': chapter.id}, status=status.HTTP_200_OK)


class SubchapterDetail(APIView):
    """
    Обработчик запросов для отдельного пользователя
    """
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JWTTokenUserAuthentication, ]

    def get_object(self, pk):
        try:
            return Subchapter.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = SubchapterSerializer(user)
        return Response(serializer.data)

    def post(self, request, format=None):
        subchapter_queryset = request.data.dict()
        subchapter_file = subchapter_queryset['file']
        subchapter_info = json.loads(subchapter_queryset['info'])
        print(subchapter_info)
        try:
            subchapter = Subchapter.objects.filter(id=subchapter_info['id'])
            if isinstance(subchapter_file, str):
                subchapter.update(name=subchapter_info['name'],
                                  number=subchapter_info['number'],
                                  chapter_id=subchapter_info['chapter_id'])
                subchapter = Subchapter.objects.get(id=subchapter_info['id'])
            else:
                subchapter.delete()
                subchapter = Subchapter.objects.create(name=subchapter_info['name'],
                                                       number=subchapter_info['number'],
                                                       body=subchapter_file,
                                                       chapter_id=subchapter_info['chapter_id'])
        except:
            subchapter = Subchapter.objects.create(name=subchapter_info['name'],
                                                   number=subchapter_info['number'],
                                                   body=subchapter_file,
                                                   chapter_id=subchapter_info['chapter_id'])
        return Response({'subchapter_id': subchapter.id}, status=status.HTTP_200_OK)


class TestList(APIView):
    """
    Обработчик запросов для списка тестов
    """
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JWTTokenUserAuthentication, ]

    def post(self, request, format=None):
        test_queryset = request.data
        print(test_queryset)
        try:
            Test.objects.filter(id=test_queryset['id']).update(title=test_queryset['title'])
            test = Test.objects.get(title=test_queryset['title'])
        except:
            test = Test.objects.create(title=test_queryset['title'])
        for question_queryset in test_queryset['question']:
            try:
                Question.objects.filter(id=question_queryset['id']).update(body=question_queryset['body'])
                question = Question.objects.get(body=question_queryset['body'], test=test)
            except:
                question = Question.objects.create(test=test, body=question_queryset['body'])
            for answer_queryset in question_queryset['answer']:
                try:
                    Answer.objects.filter(id=answer_queryset['id']).update(body=answer_queryset['body'],
                                                                           choice=answer_queryset['choice'])
                except:
                    Answer.objects.create(question=question, body=answer_queryset['body'],
                                          choice=answer_queryset['choice'])
        return Response({'test_id': test.id}, status=status.HTTP_200_OK)


class TestDetail(APIView):
    """
    Обработчик запросов для отдельного теста
    """
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JWTTokenUserAuthentication, ]

    def get_object(self, pk):
        try:
            return Test.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = ResultTestSerializer(user)
        return Response(serializer.data)
