from django.urls import path

from api.views import(
    DiciplineDetailView,
    DiciplineListView,
    GroupDetailView,
    GroupListView,
    StudentDetailView,
    StudentListView,
    TeacherDetailView,
    TeacherListView,
    UserDetailView,
    UserListView,
) 

urlpatterns = [
    path('users/', UserListView.as_view()),
    path('users/<int:pk>', UserDetailView.as_view()),
    path('groups/', GroupListView.as_view()),
    path('groups/<int:pk>', GroupDetailView.as_view()),
    path('students/', StudentListView.as_view()),
    path('students/<int:pk>', StudentDetailView.as_view()),
    path('diciplines/', DiciplineListView.as_view()),
    path('diciplines/<int:pk>', DiciplineDetailView.as_view()),
    path('teachers/', TeacherListView.as_view()),
    path('teachers/<int:pk>', TeacherDetailView.as_view()),
]