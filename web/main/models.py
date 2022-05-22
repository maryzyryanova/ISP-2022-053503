from django.db import models


class Bell(models.Model):
    pair = models.PositiveSmallIntegerField("Номер пары", default=0)
    start = models.TimeField("Начало")
    duration = models.DurationField("Длительность")

    def __str__(self) -> str:
        return f"Звонок на {self.pair} в {self.start}"

    class Meta:
        verbose_name_plural = "Звонки"
        verbose_name = "Звонок"


class Dicipline(models.Model):
    title = models.CharField("Название", max_length=200)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = "Дисциплины"
        verbose_name = "Дисциплина"


class Teacher(models.Model):
    name = models.CharField("Имя", max_length=50)
    second_name = models.CharField("Отчество", max_length=50)
    surname = models.CharField("Фамилия", max_length=50)
    photo = models.ImageField("Фото",upload_to = "media/teachers/", blank=True)
    rang = models.CharField("Должность", max_length=200)
    email = models.EmailField("Электронная почта", max_length=200)
    diciplines = models.ManyToManyField(Dicipline, verbose_name="Дисциплины")

    def __str__(self) -> str:
        return self.name 

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
    group = models.ForeignKey(Group, verbose_name="Расписание", null=True, on_delete=models.SET_NULL)
    teacher = models.ForeignKey(Teacher, verbose_name="Преподаватель", null=True, on_delete=models.SET_NULL)
    dicipline = models.ForeignKey(Dicipline, verbose_name="Дисциплина", null=True, on_delete=models.SET_NULL)
    bell = models.ForeignKey(Bell, verbose_name="Звонок", null=True, on_delete=models.SET_NULL)
    classroom = models.PositiveSmallIntegerField("Аудитория", default=0)
    day = models.PositiveSmallIntegerField("День недели", default=0)
    week = models.PositiveSmallIntegerField("Неделя", default=0)

    def __str__(self) -> str:
        return f"Пара {self.dicipline}"

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписание"

class Student(models.Model):
    name = models.CharField("Имя", max_length=50)
    second_name = models.CharField("Отчество", max_length=50)
    surname = models.CharField("Фамилия", max_length=50)
    photo = models.ImageField("Фото",upload_to = "media/students/")
    rating = models.FloatField("Рейтинг")
    number = models.CharField("Студенческий билет", max_length=15)
    group = models.ForeignKey(Group, verbose_name="Номер группы", null=True, on_delete=models.SET_NULL, blank=True)

    def __str__(self) -> str:
        return self.name 

    class Meta:
        verbose_name_plural = "Студенты"
        verbose_name = "Студент"

