import logging
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
from django.views.generic import DetailView, CreateView, DeleteView
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
from main.mixins import StudentAccessMixin, TeacherAccessMixin
from main.forms import ExamMarksForm

from .models import (
    Dicipline,
    Exam,
    ExamMark,
    Mark,
    Missings,
    Notification,
    Schedule,
    Student,
    Teacher,
    Group,
)

logger = logging.getLogger('__name__')

def main(request):
    logger.info("main success!")
    return render(request, "main_window.html")

class UserLoginView(LoginView):
    template_name = "registration/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("account")
    logger.info("UserLoginView success!")

    def get_success_url(self):
        logger.info("get_success_url success!")
        return self.success_url

class StudentsListView(ListView):
    def get(self, request):
        students = Student.objects.all()
        logger.info("StudentListView success!")
        return render(request, "students/student_list.html", {"student_list": students})

class TeachersView(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        logger.info("TeachersView success!")
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
            logger.info("ScheduleView success!")
            return render(
                request, 
                "schedule_list.html", 
                {
                    "schedule": l,
                    'group': get_object_or_404(Group, number=_id),
                }
            )
        logger.error("SchudleView: no id!")
        return render(request, "schedule_list.html")

class StudentView(DetailView):
    model = Student
    template_name = "students/student_page.html"

    def get_object(self):
        _id = self.kwargs.get("student_id")
        logger.info("StudentView success!")
        return get_object_or_404(Student, id=_id)

class TeacherView(DetailView):
    model = Teacher
    template_name = "teachers/teacher_page.html"

    def get_object(self):
        _id = self.kwargs.get("teacher_id")
        logger.info("TeacherView success!")
        return get_object_or_404(Teacher, id=_id)

class AccountView(View):
    template_name = "account.html"

    def get(self, request):
        logger.info("AccountView success!")
        return render(request, self.template_name)

class UserLogoutView(LogoutView):
    next_page = reverse_lazy("main")
    logger.info("UserLogoutView success!")

class EditView(UpdateView):
    template_name = "edit.html"
    success_url = "/account/"

    def get_object(self, queryset=None):
        if hasattr(self.request.user, "student"):
            self.form_class = EditStudentForm
            self.model = Student
            logger.info("EditVew for student success!")
            return self.request.user.student
        elif hasattr(self.request.user, "teacher"):
            self.form_class = EditTeacherForm
            self.model = Teacher
            logger.info("EditView for teacher success!")
            return self.request.user.teacher

class MarksView(StudentAccessMixin, View):
    template_name = "marks.html"

    def get(self, request, *args, **kwargs):
        group = request.user.student.group
        schedule = Schedule.objects.filter(group=group)
        logger.info("MarksView success!")
        marks = self.get_all_marks()
        return render(
            request, 
            self.template_name, 
            {
                "schedule": schedule, 
                'marks': marks, 
            }
        )

    def get_all_marks(self):
        diciplines = Schedule.objects.filter(group=self.request.user.student.group).values('dicipline__title').annotate(dcount=Count("dicipline__title"))
        res = {}
        for dicipline in diciplines:
            dic = []
            for mark in Mark.objects.filter(student=self.request.user.student, dicipline__title=dicipline['dicipline__title']):
                dic.append(mark.mark)
            s = 0
            for missing in Missings.objects.filter(student=self.request.user.student, dicipline__title=dicipline['dicipline__title']):
                s+=missing.hours
            res[dicipline['dicipline__title']] = (s, dic)
        return res

class GroupScheduleView(StudentAccessMixin, View):
    template_name = "group_schedule.html"

    def get(self, request):
        # schedule = Schedule.objects.filter(group=request.user.student.group)
        logger.info("GroupScheduleView success!")
        _id = request.user.student.group.number
        schedule = Schedule.objects.filter(group__number=_id)
        l = []
        for i in range(1, 5):
            l.append(schedule.filter(week=i))
        return render(
            request, 
            self.template_name, 
            {
                "schedule": l,
                'group': request.user.student.group,
            }
        )

class ExamsView(StudentAccessMixin, View):
    template_name = "exams.html"

    def get(self, request):
        exams = ExamMark.objects.filter(student=request.user.student)
        logger.info("ExamsView success!")
        return render(request, self.template_name, {"exams": exams})

class StudentNotificationsView(StudentAccessMixin, LoginRequiredMixin, ListView):
    template_name = "notify.html"
    model = Notification 

    def get_queryset(self):
        return self.model.objects.filter(group=self.request.user.student.group)

class StudentCurrentNotificationView(StudentAccessMixin, View):
    template_name = 'student_notification.html'
    model = Notification

    def get(self, request, *args, **kwargs):
        notification_id = self.kwargs.get("notification_id")
        notification = Notification.objects.get(id=notification_id)

        return render(
            request,
            self.template_name,
            {'notification': notification}
        ) 

class ChangePasswordView(PasswordChangeView):
    success_url = reverse_lazy("password_change_done")
    template_name = "password_change.html"
    logger.info("ChangePasswordView success!")

class ChangePasswordDone(PasswordChangeDoneView):
    template_name = "password_change_done.html"
    logger.info("ChangePasswordDone success!")

class TeacherGroupsView(TeacherAccessMixin, View):
    template_name = "teachers/teacher_groups.html"

    def get(self, request, *args, **kwargs):
        teacher = request.user.teacher
        groups = (
            Schedule.objects.filter(teacher=teacher)
            .values("group__number")
            .annotate(dcount=Count("group"))
        )
        logger.info("TeacherGroupsView success!")
        return render(
            request,
            self.template_name,
            {
                "groups": groups,
            },
        )

class TeacherGroupDiciplinesDetailView(TeacherAccessMixin, DetailView):
    template_name = "teachers/teacher_group.html"

    def get_object(self):
        _id = self.kwargs.get("group_id")
        logger.info("TeacherGroupDiciplinesDetailView get_object success!")
        return get_object_or_404(Group, number=_id)

    def get(self, request, *args, **kwargs):
        group = self.get_object()
        diciplines_new = (
            Schedule.objects.filter(group=group, teacher=request.user.teacher)
            .values("dicipline__title", "dicipline__id")
            .annotate(count=Count("dicipline"))
        )
        logger.info("TeacherGroupDiciplinesDetailView get success!")

        return render(
            request,
            self.template_name,
            {
                "diciplines": diciplines_new,
                "group": group,
            },
        )

class TeacherGroupDiciplinesListView(TeacherAccessMixin, View):
    template_name = "teachers/teacher_group_list.html"

    def get(self, request, *args, **kwargs):
        dicipline_id = self.kwargs.get("subject_id")
        group_id = self.kwargs.get("group_id")
        
        group = Group.objects.get(number=group_id)
        dicipline = Dicipline.objects.get(id=dicipline_id)
        logger.info("TeacherGroupDiciplinesListView get success!")
        return render(
            request, self.template_name, {"group": group, "dicipline": dicipline}
        )

class TeacherStudentView(TeacherAccessMixin, View):
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
        print(request.POST)
        dates = get_pairs(dicipline, group)
        dates_str = [(date.strftime("%d.%m"), date.date()) for date in dates] 
        if form.is_valid(): 
            if form.cleaned_data['mark']:
                mark,_ = Mark.objects.get_or_create(
                    student=form.cleaned_data["student"],
                    date=form.cleaned_data["date"],
                    dicipline=dicipline,
                )
                if mark.mark < 11:
                    mark.mark = form.cleaned_data["mark"]
                    mark.save()

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

class TeacherPersonalScheduleView(TeacherAccessMixin, View):
    template_name = "teachers/teacher_schedule_groups.html"
    
    def get(self, request, *args, **kwargs):
        schedule = Schedule.objects.filter(teacher=request.user.teacher)
        l = []
        for i in range(1, 5):
            l.append(schedule.filter(week=i))
        return render(request, self.template_name, {"schedule": l})

class SendNotificationView(TeacherAccessMixin, View):
    template_name = "teachers/teacher_send_notification.html"

    def get(self, request, *args, **kwargs):
        groups = (
            Schedule.objects.filter(teacher=request.user.teacher)
            .values("group__number")
            .annotate(dcount=Count("group"))
        )
        form = MessageForm(groups)
        return render(
                request,
                self.template_name,
                {
                    "groups": groups,
                    "form": form,
                },
            )
    
    def get_object(self, number):
        return get_object_or_404(Group, number=number)

    def post(self, request, *args, **kwargs):
        groups = (
            Schedule.objects.filter(teacher=request.user.teacher)
            .values("group__number")
            .annotate(dcount=Count("group"))
        )
        form = MessageForm(groups, request.POST)
        if form.is_valid():
            if form.cleaned_data['message']:
                notification,_ = Notification.objects.get_or_create(
                    teacher = request.user.teacher,
                    message = form.cleaned_data['message'],
                    group = Group.objects.get(number=form.cleaned_data['group']),
                )
                notification.save()
                return redirect('/teachers/notifications/')
        return render(
                request,
                self.template_name,
                {
                    "groups": groups,
                    "form": form,
                },
            )


class NotificationListView(TeacherAccessMixin, ListView):
    template_name = 'notifications/listview.html'
    model = Notification

    def get_queryset(self):
        return self.model.objects.filter(teacher=self.request.user.teacher)

class NotificationView(TeacherAccessMixin, View):
    template_name = 'teacher_notification.html'
    model = Notification

    def get(self, request, *args, **kwargs):
        notification_id = self.kwargs.get("notification_id")
        notification = Notification.objects.get(id=notification_id)

        return render(
            request,
            self.template_name,
            {'notification': notification}
        )

class NotificationUpdateView(TeacherAccessMixin, View):
    template_name = "teachers/teacher_send_notification.html"
    model = Notification

    def get(self, request, *args, **kwargs):
        notification_id = self.kwargs.get("notification_id")
        notification = Notification.objects.get(id=notification_id)
        groups = (
            Schedule.objects.filter(teacher=request.user.teacher)
            .values("group__number")
            .annotate(dcount=Count("group"))
        )
        data = {
            'message': notification.message,
            'group': notification.group
        }
        form = MessageForm(groups, initial = data)
        return render(
                request,
                self.template_name,
                {
                    "notification": notification,
                    "form": form,
                },
            )

    def get_object(self, id):
        return get_object_or_404(Notification, id=id)

    def post(self, request, *args, **kwargs):
        notification_id = self.kwargs.get("notification_id")
        notification = self.get_object(notification_id)
        groups = (
            Schedule.objects.filter(teacher=request.user.teacher)
            .values("group__number")
            .annotate(dcount=Count("group"))
        )
        form = MessageForm(groups, request.POST)
        if form.is_valid():
            notification.message = form.cleaned_data['message']
            notification.group = Group.objects.get(number=form.cleaned_data['group'])
            notification.save()
            return redirect('http://localhost:8000/teachers/notifications/')
        return render(
                request,
                self.template_name,
                {
                    "notification": notification,
                    "form": form,
                },
            )

class NotificationDeleteView(TeacherAccessMixin, DeleteView):
    model = Notification
    template_name = 'teacher_del_notification.html'
    success_url = reverse_lazy('teacher_notifications_list')

class TeacherGroupsExamsView(TeacherAccessMixin, View):
    template_name = "teacher_exams_group.html"

    def get(self, request, *args, **kwargs):
        teacher = request.user.teacher
        groups = (
            Exam.objects.filter(teacher=teacher)
            .values("group__number")
            .annotate(dcount=Count("group"))
        )
        logger.info("TeacherGroupsExamsView success!")
        return render(
            request,
            self.template_name,
            {
                "groups": groups,
            },
        )

class TeacherExamsView(TeacherAccessMixin, View):
    model = Exam
    template_name = 'teacher_exams.html'

    def get_object(self):
        _id = self.kwargs.get("group_id")
        logger.info("TeacherExamsView get_object success!")
        return get_object_or_404(Group, number=_id)

    def get(self, request, *args, **kwargs):
        group = self.get_object()
        exams = (
            Exam.objects.filter(group=group, teacher=request.user.teacher)
            .values("dicipline__title", "dicipline__id")
            .annotate(count=Count("dicipline"))
        )
        logger.info("TeacherExamsView get success!")

        return render(
            request,
            self.template_name,
            {
                "exams": exams,
                "group": group,
            },
        )

class TeacherExamMarksView(TeacherAccessMixin, View):
    template_name = "teacher_exam_mark.html"

    def get_object(self):
        _id = self.kwargs.get("group_id")
        return get_object_or_404(Group, number=_id)

    def get(self, request, *args, **kwargs):
        group = self.get_object()
        exam_id = self.kwargs.get("exam_id")
        sub = Dicipline.objects.get(id=exam_id)
        exam = Exam.objects.get(dicipline=sub, group=group)
        form = ExamMarksForm(group)
        exam_marks = self.get_exam_marks(exam, group)
        return render(
            request, 
            self.template_name,
            {
                "group": group,
                "exam_marks": exam_marks,
                "form": form,
            }
        )

    def get_exam_marks(self, exam, group):
        result = {}
        for student in group.students.all():
            exam_mark = student.exam_marks.filter(exam=exam)
            if exam_mark.count():
                result[student] = exam_mark[0].mark
            else:
                result[student] = ""
        return result

    def post(self, request, *args, **kwargs):
        group = self.get_object()
        exam_id = self.kwargs.get("exam_id")
        sub = Dicipline.objects.get(id=exam_id)
        exam = Exam.objects.get(dicipline=sub, group=group)
        form = ExamMarksForm(group, request.POST)
        if form.is_valid():
            if form.cleaned_data['mark']:
                exam_mark,_ = ExamMark.objects.get_or_create(
                    student=form.cleaned_data["student"],
                    exam = exam
                )
                if exam_mark.mark < 11:
                    exam_mark.mark = form.cleaned_data['mark']
                    exam_mark.save()
            return redirect(f'/teachers/exams/{group.number}/{exam_id}/')
        exam_marks = self.get_exam_marks(exam, group)
        return render(
            request, 
            self.template_name,
            {
                "group": group,
                "exam_marks": exam_marks,
                "form": form,
            }
        )



    