from datetime import timedelta
from django.test import Client, TestCase

from main.models import Mark, Student
from main.models import Missings
from .utils import get_pairs
from main.models import Dicipline, Schedule, Teacher, Group, Bell, User

# Create your tests here.

class UtilsTestCase(TestCase):
    def setUp(self):
        self.maxDiff =None
        group = Group(
            number = '1',
            faculty = 'fghjkl;',
            specialisation = 'fhgjhkjlk',
            course = 1,
        )
        group.save()

        dicipline = Dicipline(title = 'sedrftyguhijk')
        dicipline.save()

        teacher = Teacher(
            name ='dxfcgvhbj',
            second_name = 'dxfcgvhjb',
            surname = 'dfjghkjh',
            rang = 'zfdxgfx',
            email = 'cdgfhjb@mail.ru'
        )
        teacher.save()

        bell = Bell(
            pair = 1,
            start = "09:00:00",
            duration = timedelta(minutes=80)
        )
        bell.save()

        schedule = Schedule(
            group = group,
            teacher = teacher,
            dicipline = dicipline,
            bell = bell,
            day = 0,
            week = 1,
        )
        schedule.save()

        schedule = Schedule(
            group = group,
            teacher = teacher,
            dicipline = dicipline,
            bell = bell,
            day = 1,
            week = 2,
        )
        schedule.save()

        schedule = Schedule(
            group = group,
            teacher = teacher,
            dicipline = dicipline,
            bell = bell,
            day = 2,
            week = 3,
        )
        schedule.save()

        schedule = Schedule(
            group = group,
            teacher = teacher,
            dicipline = dicipline,
            bell = bell,
            day = 3,
            week = 4,
        )
        schedule.save()

    def test_time(self):
        dicipline = Dicipline.objects.get(id=1)
        group = Group.objects.get(id=1)
        approved = [
            '07.09',
            '15.09',
            '23.09',
            '27.09',
            '05.10',
            '13.10',
            '21.10',
            '25.10',
            '02.11',
            '10.11',
            '18.11',
            '22.11',
            '30.11',
            '08.12',
            '16.12',
            '20.12',
            '28.12',
        ]
        res = [ i.strftime("%d.%m") for i in get_pairs(dicipline, group)]
        self.assertEqual(res, approved)

class ViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password="password")
        self.client = Client(enforce_csrf_checks=False)
        self.client.force_login(self.user)

        group = Group(
            number = '1',
            faculty = 'fghjkl;',
            specialisation = 'fhgjhkjlk',
            course = 1,
        )
        group.save()

        self.student = Student(
            name = 'cfghvjb',
            second_name = 'fghj',
            surname = 'tctvjk',
            rating = 9.3,
            number = '05350067',
            group = group,
        )
        self.student.save()

        dicipline = Dicipline(title = 'sedrftyguhijk')
        dicipline.save()

        mark = Mark(
            mark = 5,
            student = self.student,
            dicipline = dicipline,
            date = "2021-09-07",
        )
        mark.save()

        teacher = Teacher(
            user = self.user,
            name ='dxfcgvhbj',
            second_name = 'dxfcgvhjb',
            surname = 'dfjghkjh',
            rang = 'zfdxgfx',
            email = 'cdgfhjb@mail.ru'
        )
        teacher.save()
        teacher.diciplines.add(dicipline)
        teacher.save()

        bell = Bell(
            pair = 1,
            start = "09:00:00",
            duration = timedelta(minutes=80)
        )
        bell.save()
        
        schedule = Schedule(
            group = group,
            teacher = teacher,
            dicipline = dicipline,
            bell = bell,
            day = 1,
            week = 2,
        )
        schedule.save()
        
        schedule = Schedule(
            group = group,
            teacher = teacher,
            dicipline = dicipline,
            bell = bell,
            day = 2,
            week = 3,
        )
        schedule.save()

    def test_view_teacher_student(self):
        resp = self.client.get('/teachers/groups/1/subject/1/')
        self.assertEqual(resp.status_code, 200)
        group = Group.objects.get(id=1)
        print(group.students.all().count())
        data = {
            'student': self.student.id,
            'date': "2021-09-15",
            'mark': 7,
            'missings': 2
        }
        resp = self.client.post('/teachers/groups/1/subject/1/', data)
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(Mark.objects.all().count(), 2)
        self.assertEqual(Missings.objects.all().count(), 1)