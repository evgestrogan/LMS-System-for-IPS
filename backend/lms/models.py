from django.db import models
from django.contrib.auth.models import User


class StudyGroup(models.Model):
    """
    Таблица в которой хранится
    информация об учебной группе
    """

    TYPE_CHOICES = (
        ('К', 'Курсанты'),
        ('С', 'Слушатели'),
        ('ПК', 'Курсы ПК'),
    )

    number = models.CharField(max_length=5,
                              verbose_name='Номер группы',
                              )
    type = models.CharField(max_length=20,
                            choices=TYPE_CHOICES,
                            verbose_name='Тип группы',
                            )

    class Meta:
        ordering = ('number',)
        verbose_name_plural = 'Учебные группы'
        verbose_name = 'Учебная группа'

    def __str__(self):
        return self.number


class Manager(models.Model):
    """
    Таблица для преподавателей,
    начальников циклов и кафедр
    """

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                verbose_name='Информация о пользователе',
                                related_name='manager',
                                limit_choices_to={'is_staff': True},
                                )
    avatar = models.ImageField(upload_to='user_photo',
                               default='user_photo/default.jpg',
                               verbose_name='Фотография пользователя',
                               )

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = 'Преподаватели'

    def __str__(self):
        return '{} {}'.format(self.user.last_name, self.user.first_name)


class Student(models.Model):
    """
    Таблица для студентов
    """

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                verbose_name='Информация о пользователе',
                                related_name='student',
                                limit_choices_to={'is_staff': False},
                                )
    avatar = models.ImageField(upload_to='user_photo',
                               default='user_photo/default.jpg',
                               verbose_name='Фотография пользователя',
                               )
    group = models.ForeignKey(StudyGroup,
                              on_delete=models.CASCADE,
                              verbose_name='Номер учебной группы',
                              related_name='user',
                              )

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return self.user.username


class Test(models.Model):
    """
    Таблица теста с полем пользователей,
    которые имеют доступ на прохождение
    данного теста
    """

    user = models.ManyToManyField(Student,
                                  verbose_name='Обучаемые',
                                  related_name='test',
                                  blank=True,
                                  )
    title = models.TextField()

    def get_amount_user(self):
        """
        функция для страницы администратора
        возвращающая количество пользователей
        имеющих доступ к данному курсу
        """
        return str(len(self.user.all()))

    class Meta:
        verbose_name = "Результирующий тест"
        verbose_name_plural = 'Результирующие тесты'

    def __str__(self):
        return self.title


class Question(models.Model):
    """
    Таблица вопросов к тестам
    """

    body = models.TextField(verbose_name='Вопрос',
                            )
    test = models.ForeignKey(Test,
                             on_delete=models.CASCADE,
                             verbose_name='Тест',
                             related_name='question',
                             )

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.body


class Answer(models.Model):
    """
    Таблица ответов на вопросы
    """

    body = models.TextField(verbose_name='Ответ',
                            )
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE,
                                 verbose_name='Вопрос',
                                 related_name='answer',
                                 )
    choice = models.BooleanField(default=False,
                                 verbose_name='Верный ли ответ?'
                                 )

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return self.body


class Department(models.Model):
    """
    Модель, реализующая кафедры в университете
    У каждой кафедры есть ее название, менеджер
    (заведующей кафедрой)
    """

    manager = models.ForeignKey(Manager,
                                on_delete=models.CASCADE,
                                verbose_name='Начальник кафедры',
                                related_name='department_manager',
                                limit_choices_to={'user__is_staff': True},
                                )
    name = models.CharField(max_length=25,
                            verbose_name='Название кафедры',
                            help_text='В родительном падеже',
                            unique=True,
                            )

    class Meta:
        ordering = ('name',)
        verbose_name = "Кафедра"
        verbose_name_plural = 'Кафедры'

    def __str__(self):
        return self.name


class Subject(models.Model):
    """
    Модель предмета (цикла) связанная с
    моделью кафедры и имеющая менеджера
    данного предмета
    """

    department = models.ForeignKey(Department,
                                   on_delete=models.CASCADE,
                                   verbose_name='Кафедра',
                                   related_name='subject',
                                   )
    name = models.CharField(max_length=50,
                            verbose_name='Название предмета',
                            unique=True,
                            )
    manager = models.ForeignKey(Manager,
                                on_delete=models.CASCADE,
                                verbose_name='Начальник цикла',
                                related_name='subject_manager',
                                limit_choices_to={'user__is_staff': True},
                                )

    class Meta:
        verbose_name_plural = 'Предметы'
        verbose_name = 'Предмет'

    def __str__(self):
        return self.name


class Course(models.Model):
    """Модель курса связанная с
    моделью предмета и включает
    в себя связь с таблицей тестов,
    студентов, записанных на курс,
    и менеджера (создателя) данного курса
    """

    subject = models.ForeignKey(Subject,
                                on_delete=models.CASCADE,
                                verbose_name='Предмет',
                                related_name='course',
                                )
    name = models.CharField(max_length=50,
                            verbose_name='Название курса',
                            unique=True,
                            )
    manager = models.ForeignKey(Manager,
                                on_delete=models.CASCADE,
                                verbose_name='Разработчик курса',
                                related_name='course_manager',
                                limit_choices_to={'user__is_staff': True},
                                )
    trainee = models.ManyToManyField(Student,
                                     verbose_name='Обучаемые',
                                     related_name='course',
                                     blank=True,
                                     )
    test = models.OneToOneField(Test,
                                verbose_name='Тест',
                                related_name='course',
                                on_delete=models.SET_NULL,
                                blank=True,
                                null=True,
                                )

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Курсы'
        verbose_name = 'Курс'

    def get_amount_trainee(self):
        """
        функция для страницы администратора
        возвращающая количество всех обучаемых на курсе
        """

        return str(len(self.trainee.all()))

    def __str__(self):
        return self.name


class Chapter(models.Model):
    """
    Таблица главы которая связанна с
    таблицей курсов и имеет свой тест
    """

    course = models.ForeignKey(Course,
                               on_delete=models.CASCADE,
                               verbose_name='Курс',
                               related_name='chapter',
                               )
    number = models.CharField(max_length=5,
                              verbose_name='Номер главы',
                              )
    name = models.CharField(max_length=150,
                            verbose_name='Название главы',
                            )
    test = models.OneToOneField(Test,
                                verbose_name='Тест',
                                related_name='chapter',
                                on_delete=models.SET_NULL,
                                blank=True,
                                null=True,
                                )

    class Meta:
        ordering = ('number', 'name',)
        verbose_name_plural = 'Главы'
        verbose_name = 'Глава'
        unique_together = ['number', 'name']

    def __str__(self):
        return "Глава {} - {}".format(self.number, self.name)


class Subchapter(models.Model):
    """
    Таблица поддглавы которая
    связанна с таблицей курсов
    """

    chapter = models.ForeignKey(Chapter,
                                on_delete=models.CASCADE,
                                verbose_name='Глава',
                                related_name='subchapter',
                                )
    number = models.CharField(max_length=5,
                              verbose_name='Номер подглавы',
                              )
    name = models.CharField(max_length=150,
                            verbose_name='Название подглавы',
                            )
    body = models.FileField(upload_to='subchapter',
                            verbose_name='DPF документ',
                            )

    class Meta:
        ordering = ('name', 'number',)
        verbose_name = 'Подглава'
        verbose_name_plural = 'Подглавы'
        unique_together = ['number', 'name']

    def __str__(self):
        return "Подглава {} - {}".format(self.number, self.name)
