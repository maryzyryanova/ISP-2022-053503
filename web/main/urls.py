from django.urls import path, include
from .views import (
    ScheduleView,
    StudentView, 
    StudentsListView,
    TeachersView, 
    TeacherView,
    main,  
    user_login)

urlpatterns = [
    path('', main),
    path('students/', StudentsListView.as_view()),
    path('teachers/', TeachersView.as_view()),
    path('schedule/', ScheduleView.as_view()),
    path('schedule/<str:schedule_id>', ScheduleView.as_view()),
    path('students/<int:student_id>', StudentView.as_view()),
    path('teachers/<int:teacher_id>', TeacherView.as_view()),
    path('login/', user_login, name = 'login')
]
