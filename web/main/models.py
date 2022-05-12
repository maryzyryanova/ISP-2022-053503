from django.db import models


class Bell(models.Model):
    pair = models.PositiveSmallIntegerField("№: ", default=0)
    start = models.TimeField()
    duration = models.DurationField()

    class Meta:
        verbose_name_plural = "Звонки"
        verbose_name = "Звонок"


class Dicipline(models.Model):
    title = models.CharField("Название: ", max_length=200)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = "Дисциплины"
        verbose_name = "Дисциплина"


class Teacher(models.Model):
    name = models.CharField("Имя: ", max_length=50)
    second_name = models.CharField("Отчество: ", max_length=50)
    surname = models.CharField("Фамилия: ", max_length=50)
    photo = models.ImageField("Фото: ",upload_to = "teachers/")
    rang = models.CharField("Должность: ", max_length=200)
    email = models.EmailField("Электронная почта: ", max_length=200)
    diciplines = models.ManyToManyField(Dicipline, verbose_name="Дисциплины: ")

    def __str__(self) -> str:
        return self.name 

    class Meta:
        verbose_name_plural = "Преподаватели"
        verbose_name = "Преподаватель"


class Group(models.Model):
    number = models.PositiveSmallIntegerField("Номер: ", default=0)
    faculty = models.CharField("Факультет: ", max_length=200)
    specialisation = models.CharField("Специальность: ", max_length=200)
    course = models.PositiveSmallIntegerField("Курс: ", default=0)

    class Meta:
        verbose_name_plural = "Группы"
        verbose_name = "Группа"

class Schedule(models.Model):
    group = models.ForeignKey(Group, verbose_name="Расписание: ", null=True, on_delete=models.SET_NULL)
    teacher = models.ForeignKey(Teacher, verbose_name="Преподаватель: ", null=True, on_delete=models.SET_NULL)
    dicipline = models.ForeignKey(Dicipline, verbose_name="Дисциплина: ", null=True, on_delete=models.SET_NULL)
    bell = models.ForeignKey(Bell, verbose_name="Звонок", null=True, on_delete=models.SET_NULL)
    classroom = models.PositiveSmallIntegerField("Аудитория: ", default=0)
    week = models.PositiveSmallIntegerField("Неделя: ", default=0)
    number = models.PositiveSmallIntegerField("№: ", default=0)

    class Meta:
        verbose_name = "Расписание"

class Student(models.Model):
    name = models.CharField("Имя: ", max_length=50)
    second_name = models.CharField("Отчество: ", max_length=50)
    surname = models.CharField("Фамилия: ", max_length=50)
    photo = models.ImageField("Фото: ",upload_to = "students/")
    rating = models.FloatField("Рейтинг: ")
    number = models.PositiveBigIntegerField("Студенческий билет: ", default=0)
    group = models.ForeignKey(Group, verbose_name="Номер группы: ", null=True, on_delete=models.SET_NULL, blank=True)

    def __str__(self) -> str:
        return self.name 

    class Meta:
        verbose_name_plural = "Студенты"
        verbose_name = "Студент"

