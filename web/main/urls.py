from django.urls import path, include
from .views import (
    EditView,
    ExamsView,
    GroupScheduleView,
    MarksView,
    NotificationsView,
    ScheduleView,
    StudentView, 
    StudentsListView,
    AccountView,
    TeachersView, 
    TeacherView,
    UserLoginView,
    UserLogoutView,
    main,
)

urlpatterns = [
    path('', main, name="main"),
    path('students/', StudentsListView.as_view()),
    path('teachers/', TeachersView.as_view()),
    path('schedule/', ScheduleView.as_view()),
    path('schedule/<str:schedule_id>', ScheduleView.as_view()),
    path('students/<int:student_id>', StudentView.as_view()),
    path('teachers/<int:teacher_id>', TeacherView.as_view()),
    path('login', UserLoginView.as_view(), name = 'login'),
    path('account', AccountView.as_view(), name='account'),
    path('logout', UserLogoutView.as_view(), name='logout'),
    path('account/edit', EditView.as_view(), name='edit'),
    path('account/group-schedule', GroupScheduleView.as_view(), name="group_schedule"),
    path('account/marks', MarksView.as_view(), name="marks"),
    path('account/exams', ExamsView.as_view(), name='exams'),
    path('account/notifications', NotificationsView.as_view(), name='notification')
]
