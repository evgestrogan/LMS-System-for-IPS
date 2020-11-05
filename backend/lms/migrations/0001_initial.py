# Generated by Django 2.2 on 2020-10-26 19:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True, verbose_name='Номер главы')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название главы')),
            ],
            options={
                'verbose_name': 'Глава',
                'verbose_name_plural': 'Главы',
                'ordering': ('name', 'number'),
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='В родительном падеже', max_length=25, unique=True, verbose_name='Название кафедры')),
            ],
            options={
                'verbose_name': 'Кафедра',
                'verbose_name_plural': 'Кафедры',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='user_photo/default.jpg', upload_to='user_photo', verbose_name='Фотография пользователя')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='manager', to=settings.AUTH_USER_MODEL, verbose_name='Информация о пользователе')),
            ],
            options={
                'verbose_name': 'Преподаватель',
                'verbose_name_plural': 'Преподаватели',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='user_photo/default.jpg', upload_to='user_photo', verbose_name='Фотография пользователя')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
            },
        ),
        migrations.CreateModel(
            name='StudyGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=5, verbose_name='Номер группы')),
                ('type', models.CharField(choices=[('К', 'Курсанты'), ('С', 'Слушатели'), ('ПК', 'Курсы ПК')], max_length=20, verbose_name='Тип группы')),
            ],
            options={
                'verbose_name': 'Учебная группа',
                'verbose_name_plural': 'Учебные группы',
                'ordering': ('number',),
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('user', models.ManyToManyField(blank=True, related_name='test', to='lms.Student', verbose_name='Обучаемые')),
            ],
            options={
                'verbose_name': 'Результирующий тест',
                'verbose_name_plural': 'Результирующие тесты',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название предмета')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to='lms.Department', verbose_name='Кафедра')),
                ('manager', models.ForeignKey(limit_choices_to={'user__is_staff': True}, on_delete=django.db.models.deletion.CASCADE, related_name='subject_manager', to='lms.Manager', verbose_name='Начальник цикла')),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предметы',
            },
        ),
        migrations.CreateModel(
            name='Subchapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True, verbose_name='Номер подглавы')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название подглавы')),
                ('body', models.FileField(upload_to='subchapter', verbose_name='DPF документ')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subchapter', to='lms.Chapter', verbose_name='Глава')),
            ],
            options={
                'verbose_name': 'Подглава',
                'verbose_name_plural': 'Подглавы',
                'ordering': ('name', 'number'),
            },
        ),
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.ForeignKey(limit_choices_to={'user__is_staff': False}, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='lms.StudyGroup', verbose_name='Номер учебной группы'),
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL, verbose_name='Информация о пользователе'),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='Вопрос')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='lms.Test', verbose_name='Тест')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.AddField(
            model_name='department',
            name='manager',
            field=models.ForeignKey(limit_choices_to={'user__is_staff': True}, on_delete=django.db.models.deletion.CASCADE, related_name='department_manager', to='lms.Manager', verbose_name='Начальник кафедры'),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название курса')),
                ('manager', models.ForeignKey(limit_choices_to={'user__is_staff': True}, on_delete=django.db.models.deletion.CASCADE, related_name='course_manager', to='lms.Manager', verbose_name='Разработчик курса')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='lms.Subject', verbose_name='Предмет')),
                ('test', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course', to='lms.Test', verbose_name='Тест')),
                ('trainee', models.ManyToManyField(blank=True, related_name='course', to='lms.Student', verbose_name='Обучаемые')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='chapter',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='lms.Course', verbose_name='Курс'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='test',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chapter', to='lms.Test', verbose_name='Тест'),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='Ответ')),
                ('choice', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='lms.Question', verbose_name='Вопрос')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
    ]
