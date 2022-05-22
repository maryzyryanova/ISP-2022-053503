from urllib import request
from django.shortcuts import redirect, render
from django.views import View
from .models import Schedule, Student, Teacher

def main(request):
    return render(request, 'main_window.html')

class StudentsView(View):
    def get(self, request):
        students = Student.objects.all()
        return render(request, "students/student_list.html", {"student_list": students})

class TeachersView(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        return render(request, "teachers_list.html", {"teachers_list": teachers})


class ScheduleView(View):
    def get(self, request):
        schedule = Schedule.objects.all()
        return render(request, "schedule_list.html", {"schedule_list": schedule})

