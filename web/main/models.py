from tabnanny import verbose
from django.db import models
import datetime
from django.contrib.auth import get_user_model

User = get_user_model()

class Bell(models.Model):
    pair = models.PositiveSmallIntegerField("Номер пары", default=0)
    start = models.TimeField("Начало")
    duration = models.DurationField("Длительность")

    def __str__(self) -> str:
        return f"Звонок на {self.pair} в {self.start}"

    class Meta:
        verbose_name_plural = "Звонки"
        verbose_name = "Звонок"

class Mark(models.Model):
    mark = models.PositiveSmallIntegerField("Отметка", default=0)
    dicipline = models.ForeignKey('Dicipline', related_name='marks', verbose_name="Дисциплины", null=True, on_delete=models.SET_NULL)
    student = models.ForeignKey('Student', related_name='marks', verbose_name='Студент', null=True, on_delete=models.SET_NULL)
    date = models.DateField("Date", default=datetime.date.today)

    class Meta:
        verbose_name = "Отметка"
        verbose_name_plural = "Отметки"

class Dicipline(models.Model):
    title = models.CharField("Название", max_length=200)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = "Дисциплины"
        verbose_name = "Дисциплина"


class Teacher(models.Model):
    user = models.OneToOneField(User, null=True, related_name='teacher', on_delete=models.CASCADE, blank=True)
    name = models.CharField("Имя", max_length=50)
    second_name = models.CharField("Отчество", max_length=50)
    surname = models.CharField("Фамилия", max_length=50)
    photo = models.ImageField("Фото",upload_to = "media/teachers/", blank=True, null=True)
    rang = models.CharField("Должность", max_length=200)
    email = models.EmailField("Электронная почта", max_length=200)
    diciplines = models.ManyToManyField(Dicipline, verbose_name="Дисциплины")

    def __str__(self) -> str:
        return f'{self.surname} {self.name} {self.second_name}'

    class Meta:
        verbose_name_plural = "Преподаватели"
        verbose_name = "Преподаватель"


class Group(models.Model):
    number = models.CharField("Номер", max_length=6)
    faculty = models.CharField("Факультет", max_length=200)
    specialisation = models.CharField("Специальность", max_length=200)
    course = models.PositiveSmallIntegerField("Курс", default=0)

    def __str__(self) -> str:
        return self.number

    class Meta:
        verbose_name_plural = "Группы"
        verbose_name = "Группа"

class Schedule(models.Model):
    DAY_CHOICE = (
        (0,'Понедельник'),
        (1,'Вторник'),
        (2,'Среда'),
        (3,'Четверг'),
        (4,'Пятница'),
        (5,'Суббота'),
        (6,'Воскресенье'),
    )

    TYPE_CHOICE = (
        ('лк', "Лекция"),
        ('пз', "Практическое занятие"),
        ('лр', "Лабораторная работа"),
    )

    group = models.ForeignKey(Group, verbose_name="Группа", null=True, on_delete=models.SET_NULL)
    teacher = models.ForeignKey(Teacher, verbose_name="Преподаватель", null=True, on_delete=models.SET_NULL)
    dicipline = models.ForeignKey(Dicipline, verbose_name="Дисциплина", null=True, on_delete=models.SET_NULL)
    bell = models.ForeignKey(Bell, verbose_name="Звонок", null=True, on_delete=models.SET_NULL)
    classroom = models.PositiveSmallIntegerField("Аудитория", default=0)
    day = models.PositiveSmallIntegerField("День недели", default=0, choices=DAY_CHOICE)
    week = models.PositiveSmallIntegerField("Неделя", default=0)
    pair_type = models.CharField("Тип", max_length=50, default='', choices=TYPE_CHOICE)

    def __str__(self) -> str:
        return f"Пара #{self.bell.pair} {self.dicipline} [{self.get_day_display()} {self.week}]"

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписание"

class Student(models.Model):
    user = models.OneToOneField(User, null=True, related_name='student', on_delete=models.CASCADE, blank=True)
    name = models.CharField("Имя", max_length=50)
    second_name = models.CharField("Отчество", max_length=50)
    surname = models.CharField("Фамилия", max_length=50)
    photo = models.ImageField("Фото",upload_to = "media/students/", null=True, blank=True)
    rating = models.FloatField("Рейтинг")
    number = models.CharField("Студенческий билет", max_length=15)
    group = models.ForeignKey(Group, related_name='students', verbose_name="Номер группы", null=True, on_delete=models.SET_NULL, blank=True)

    def __str__(self) -> str:
        return f'{self.surname} {self.name} {self.second_name}'

    class Meta:
        ordering = ('surname','name','second_name')
        verbose_name_plural = "Студенты"
        verbose_name = "Студент"

class Exam(models.Model):
    group = models.ForeignKey(Group, verbose_name="Номер группы", null=True, on_delete=models.CASCADE, blank=True) 
    dicipline = models.OneToOneField(Dicipline, verbose_name="Дисциплина", null=True, on_delete=models.CASCADE, blank=True)
    exam_type = models.CharField("Тип", max_length=50)
    classroom = models.PositiveSmallIntegerField("Аудитория", default=0)
    day = models.PositiveSmallIntegerField("День недели", default=0)
    bell = models.ForeignKey(Bell, verbose_name="Звонок", null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return f"Экзамен по {self.dicipline}"

    class Meta:
        verbose_name_plural = "Экзамены"
        verbose_name = "Экзамен"

class ExamMark(models.Model):
    mark = models.PositiveSmallIntegerField("Отметка", default=0)
    exam = models.OneToOneField('Exam', related_name='marks', verbose_name="Отметки", null=True, on_delete=models.CASCADE)    
    student = models.ForeignKey('Student', related_name='exam_marks', verbose_name='Студент', null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Экзаменационная отметка"
        verbose_name_plural = "Экзаменационные отметки"

class Notification(models.Model):
    teacher = models.ForeignKey(Teacher, related_name="notifications", verbose_name="Преподаватель", null=True, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, related_name="notifications", verbose_name="Преподаватель", null=True, on_delete=models.CASCADE)
    message = models.TextField("Сообщение")

class Missings(models.Model):
    hours = models.PositiveSmallIntegerField("Количество")
    dicipline = models.ForeignKey(Dicipline, related_name="missings", verbose_name="Пропуски", null=True, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name="missings", verbose_name="Пропуски", null=True, on_delete=models.CASCADE)
    date = models.DateField("Date", default=datetime.date.today)

    class Meta:
        verbose_name = "Часы пропусков"