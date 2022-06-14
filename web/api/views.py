from rest_framework import generics
from django.contrib.auth import get_user_model

from api.serializers import (
    DiciplineSerialize, 
    GroupSerializer, 
    StudentSerializer, 
    TeacherSerializer, 
    UserSerializer
)

from main.models import(
    Dicipline, 
    Group, 
    Student, 
    Teacher
) 

User = get_user_model()

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupListView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class DiciplineListView(generics.ListAPIView):
    queryset = Dicipline.objects.all()
    serializer_class = DiciplineSerialize

class DiciplineDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dicipline.objects.all()
    serializer_class = DiciplineSerialize

class TeacherListView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer