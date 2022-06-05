from django.contrib import admin
from .models import Bell, Dicipline, Exam, ExamMark, Mark, Missings, Notification, Teacher, Student, Schedule, Group

admin.site.register(Bell)
admin.site.register(Dicipline)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Schedule)
admin.site.register(Group)
admin.site.register(Mark)
admin.site.register(Exam)
admin.site.register(ExamMark)
admin.site.register(Missings)
admin.site.register(Notification)