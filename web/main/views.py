from tkinter.messagebox import NO
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View, CreateView
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


from main.forms import LoginForm, EditTeacherForm, EditStudentForm, MessageForm
from .models import ExamMark, Notification, Schedule, Student, Teacher

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

class TeacherView(DetailView):
    model = Teacher
    template_name = "teachers/teacher_page.html"
    def get_object(self):
        _id = self.kwargs.get("teacher_id")
        return get_object_or_404(Teacher, id = _id) 

class AccountView(View):
    template_name = "account.html"

    def get(self, request):
        return render(request, self.template_name)

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('main')

class EditView(UpdateView):
    template_name = "edit.html"
    def get_object(self, queryset=None):
        if self.request.user.student:
            self.form_class = EditStudentForm
            self.model = Student
            return self.request.user.student
        elif self.request.user.teacher:
            self.form_class = EditTeacherForm
            self.model = Teacher
            return self.request.user.teacher
        
class MarksView(View):
    template_name = "marks.html"
    def get(self, request, *args, **kwargs):
        group = request.user.student.group
        schedule = Schedule.objects.filter(group = group)
        return render(request, self.template_name, {"schedule": schedule})

class GroupScheduleView(View):
    template_name = "group_schedule.html"
    def get(self, request):
        schedule = Schedule.objects.filter(group = request.user.student.group)
        return render(request, self.template_name, {"schedule": schedule})

class ExamsView(View):
    template_name = "exams.html"
    def get(self, request):
        exams = ExamMark.objects.filter(student = request.user.student)
        return render(request, self.template_name, {"exams": exams})

class NotificationsView(LoginRequiredMixin, CreateView):
    template_name = 'notify.html'
    model = Notification
    form_class = MessageForm
    login_url = '/login'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            ticket = Notification()
            ticket.user = request.user.profile
            ticket.email = form.cleaned_data['email']
            ticket.issue = form.cleaned_data['issue']
            ticket.message = form.cleaned_data['message']
            ticket.save()
            return redirect('/')

        return render(
            request,
            self.template_name,
            {
                'form': form,
            }
        )

    def get(self, request, *args, **kwargs):
        form = self.form_class()

        return render(
            request,
            self.template_name,
            {
                'form': form,
            }
        )

class ChangePasswordView(PasswordChangeView):
    success_url = reverse_lazy('password_change_done')
    template_name = 'password_change.html'

class ChangePasswordDone(PasswordChangeDoneView):
    template_name = 'password_change_done.html'