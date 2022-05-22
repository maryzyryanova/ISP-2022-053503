from django.urls import path, include
from .views import ScheduleView, StudentsView, TeachersView, main

urlpatterns = [
    path('', main),
    path('students/', StudentsView.as_view()),
    path('teachers/', TeachersView.as_view()),
    path('schedule/', ScheduleView.as_view()),
]
