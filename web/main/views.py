import numbers
from tokenize import group
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
)
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import DetailView, CreateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from main.utils import get_pairs


from main.forms import (
    LoginForm,
    EditTeacherForm,
    EditStudentForm,
    MessageForm,
    MarksForm,
)

from .models import (
    Dicipline,
    ExamMark,
    Mark,
    Missings,
    Notification,
    Schedule,
    Student,
    Teacher,
    Group,
)

def main(request):
    return render(request, "main_window.html")

class UserLoginView(LoginView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = reverse_lazy("account")

    def get_success_url(self):
        return self.success_url

class StudentsListView(ListView):
    def get(self, request):
        students = Student.objects.all()
        return render(request, "students/student_list.html", {"student_list": students})

class TeachersView(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        return render(
            request, "teachers/teachers_list.html", {"teachers_list": teachers}
        )

class ScheduleView(View):
    def get(self, request, *args, **kwargs):
        _id = self.kwargs.get("schedule_id")
        if _id:
            schedule = Schedule.objects.filter(group__number=_id)
            l = []
            for i in range(1, 5):
                l.append(schedule.filter(week=i))
            return render(request, "schedule_list.html", {"schedule": l})
        return render(request, "schedule_list.html")

class StudentView(DetailView):
    model = Student
    template_name = "students/student_page.html"

    def get_object(self):
        _id = self.kwargs.get("student_id")
        return get_object_or_404(Student, id=_id)

class TeacherView(DetailView):
    model = Teacher
    template_name = "teachers/teacher_page.html"

    def get_object(self):
        _id = self.kwargs.get("teacher_id")
        return get_object_or_404(Teacher, id=_id)

class AccountView(View):
    template_name = "account.html"

    def get(self, request):
        return render(request, self.template_name)

class UserLogoutView(LogoutView):
    next_page = reverse_lazy("main")

class EditView(UpdateView):
    template_name = "edit.html"
    success_url = "/account/"

    def get_object(self, queryset=None):
        print(dir(self.request.user))
        if hasattr(self.request.user, "student"):
            self.form_class = EditStudentForm
            self.model = Student
            return self.request.user.student
        elif hasattr(self.request.user, "teacher"):
            self.form_class = EditTeacherForm
            self.model = Teacher
            return self.request.user.teacher

class MarksView(View):
    template_name = "marks.html"

    def get(self, request, *args, **kwargs):
        group = request.user.student.group
        schedule = Schedule.objects.filter(group=group)
        return render(request, self.template_name, {"schedule": schedule})

class GroupScheduleView(View):
    template_name = "group_schedule.html"

    def get(self, request):
        schedule = Schedule.objects.filter(group=request.user.student.group)
        return render(request, self.template_name, {"schedule": schedule})

class ExamsView(View):
    template_name = "exams.html"

    def get(self, request):
        exams = ExamMark.objects.filter(student=request.user.student)
        return render(request, self.template_name, {"exams": exams})

class NotificationsView(LoginRequiredMixin, CreateView):
    template_name = "notify.html"
    model = Notification
    form_class = MessageForm
    login_url = "/login"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            ticket = Notification()
            ticket.user = request.user.profile
            ticket.email = form.cleaned_data["email"]
            ticket.issue = form.cleaned_data["issue"]
            ticket.message = form.cleaned_data["message"]
            ticket.save()
            return redirect("/")

        return render(
            request,
            self.template_name,
            {
                "form": form,
            },
        )

    def get(self, request, *args, **kwargs):
        form = self.form_class()

        return render(
            request,
            self.template_name,
            {
                "form": form,
            },
        )

class ChangePasswordView(PasswordChangeView):
    success_url = reverse_lazy("password_change_done")
    template_name = "password_change.html"

class ChangePasswordDone(PasswordChangeDoneView):
    template_name = "password_change_done.html"

class TeacherGroupsView(View):
    template_name = "teachers/teacher_groups.html"

    def get(self, request, *args, **kwargs):
        teacher = request.user.teacher
        groups = (
            Schedule.objects.filter(teacher=teacher)
            .values("group__number")
            .annotate(dcount=Count("group"))
        )

        return render(
            request,
            self.template_name,
            {
                "groups": groups,
            },
        )

class TeacherGroupDiciplinesDetailView(DetailView):
    template_name = "teachers/teacher_group.html"

    def get_object(self):
        _id = self.kwargs.get("group_id")
        return get_object_or_404(Group, number=_id)

    def get(self, request, *args, **kwargs):
        # diciplines = Dicipline.objects.all()
        group = self.get_object()
        diciplines_new = (
            Schedule.objects.filter(group=group, teacher=request.user.teacher)
            .values("dicipline__title", "dicipline__id")
            .annotate(count=Count("dicipline"))
        )
        return render(
            request,
            self.template_name,
            {
                "diciplines": diciplines_new,
                "group": group,
            },
        )

class TeacherGroupDiciplinesListView(View):
    template_name = "teachers/teacher_group_list.html"

    def get(self, request, *args, **kwargs):
        dicipline_id = self.kwargs.get("subject_id")
        group_id = self.kwargs.get("group_id")

        group = Group.objects.get(number=group_id)
        dicipline = Dicipline.objects.get(id=dicipline_id)
        return render(
            request, self.template_name, {"group": group, "dicipline": dicipline}
        )

class TeacherStudentView(View):
    template_name = "teachers/teacher_student.html"

    def get_object(self):
        _id = self.kwargs.get("group_id")
        return get_object_or_404(Group, number=_id)

    def get(self, request, *args, **kwargs):
        group = self.get_object()
        dicipline_id = self.kwargs.get("subject_id")
        dicipline = Dicipline.objects.get(id=dicipline_id)
        form = MarksForm(group, dicipline)
        marks = self.get_all_marks()
        dates = get_pairs(dicipline, group)
        dates_str = [(date.strftime("%d.%m"), date.date()) for date in dates] 
        return render(
            request,
            self.template_name,
            {
                "group": group,
                "marks": marks,
                "form": form,
                "dates": dates_str,
            },
        )

    def get_all_marks(self):
        dicipline_id = self.kwargs.get("subject_id")
        dicipline = Dicipline.objects.get(id=dicipline_id)
        group = self.get_object()
        dates = get_pairs(dicipline, group)
        dates_str = [date.date() for date in dates]
        res = {}
        for student in group.students.all():
            marks = {}
            for date in dates_str:
                mark = student.marks.filter(dicipline=dicipline, date=date)
                missings = student.missings.filter(dicipline=dicipline, date=date)
                if missings.count() and mark.count():
                    marks[date] = f'{mark[0].mark}/{missings[0].hours} ч.'
                elif missings.count():
                    marks[date] = f'{missings[0].hours} ч.'
                elif mark.count():
                    marks[date] = mark[0].mark
                else:
                    marks[date] = ""
            res[student] = marks
        return res

    def post(self, request, *args, **kwargs):
        dicipline_id = self.kwargs.get("subject_id")
        dicipline = Dicipline.objects.get(id=dicipline_id)
        group = self.get_object()
        form = MarksForm(group, dicipline, request.POST)
        dates = get_pairs(dicipline, group)
        dates_str = [(date.strftime("%d.%m"), date.date()) for date in dates] 
        if form.is_valid():
            print(form.cleaned_data['mark'], form.cleaned_data['missings'])
            if form.cleaned_data['mark']:
                mark,_ = Mark.objects.get_or_create(
                    student=form.cleaned_data["student"],
                    date=form.cleaned_data["date"],
                    dicipline=dicipline,
                )
                if mark.mark < 11:
                    mark.mark = form.cleaned_data["mark"]
                    mark.save()
                    return redirect(f'/teachers/groups/{group.number}/subject/{dicipline_id}')

            if form.cleaned_data['missings']:
                missings,_ = Missings.objects.get_or_create(
                    student=form.cleaned_data["student"],
                    date=form.cleaned_data["date"],
                    dicipline=dicipline,
                )
                missings.hours = form.cleaned_data['missings']
                missings.save()
                return redirect(f'/teachers/groups/{group.number}/subject/{dicipline_id}')
        marks = self.get_all_marks()
        return render(
                request,
                self.template_name,
                {
                    "group": group,
                    "marks": marks,
                    "form": form,
                    "dates": dates_str,
                },
            )

class TeacherPersonalScheduleView(View):
    template_name = "teachers/teacher_schedule_groups.html"
    
    def get(self, request, *args, **kwargs):
        schedule = Schedule.objects.filter(teacher=request.user.teacher)
        l = []
        for i in range(1, 5):
            l.append(schedule.filter(week=i))
        return render(request, self.template_name, {"schedule": l})