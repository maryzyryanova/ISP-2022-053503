from urllib import request
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView


from main.forms import LoginForm
from .models import Schedule, Student, Teacher

def main(request):
    return render(request, 'main_window.html')

class UserLoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('account')

    def get_success_url(self):
        return self.success_url

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

class AccountView(View):
    template_name = "account.html"

    def get(self, request):
        return render(
            request,
            self.template_name
        )

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('main')

class EditView(UpdateView):
    template_name = "edit.html"
    if request.user.student:
        field = ['']

class MarksView(View):
    pass

class GroupScheduleView(View):
    pass

class ExamsView(View):
    pass

class NotificationsView(View):
    pass
