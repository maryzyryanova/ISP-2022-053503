from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import DetailView

from main.forms import LoginForm
from .models import Schedule, Student, Teacher

def main(request):
    return render(request, 'main_window.html')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # return redirect тут я хз 
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

class StudentsListView(ListView):
    def get(self, request):
        students = Student.objects.all()
        return render(request, "students/student_list.html", {"student_list": students})

class TeachersView(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        return render(request, "teachers/teachers_list.html", {"teachers_list": teachers})

class ScheduleView(View):
    def get(self, request, *args, **kwargs):
        _id = self.kwargs.get("schedule_id")
        if _id:
            schedule = Schedule.objects.filter(group__number = _id)
            return render(request, "schedule_list.html", {"schedule_list": schedule})
        return render(request, "schedule_list.html")

class StudentView(DetailView):
    model = Student
    template_name = "students/student_page.html"
    def get_object(self):
        _id = self.kwargs.get("student_id")
        return get_object_or_404(Student, id = _id) 

    # def get(self, request):
    #     print(self.kwargs.get("student_id"))
    #     student = Student.objects.all() #как передавать конкретного пользователя?
    #     return render(request, "students/student_page.html", {"student_page": student})

class TeacherView(DetailView):
    model = Teacher
    template_name = "teachers/teacher_page.html"
    def get_object(self):
        _id = self.kwargs.get("teacher_id")
        return get_object_or_404(Teacher, id = _id) 

class UserView(View):
    pass


