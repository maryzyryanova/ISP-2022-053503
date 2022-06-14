from rest_framework import serializers
from django.contrib.auth import get_user_model

from main.models import (
    Dicipline, 
    Group, 
    Teacher, 
    Student
) 

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 
            'username'
        )

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = (
            'number',
            'faculty',
            'specialisation',
            'course',
        )

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    group = GroupSerializer(many = True)
    class Meta:
        model = Student
        fields = (
            'user',
            'name',
            'second_name',
            'surname',
            'photo',
            'number',
            'group',
        )

class DiciplineSerialize(serializers.ModelSerializer):
    class Meta:
        model = Dicipline
        fields = ('title', )

class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    diciplines = DiciplineSerialize(many = True)
    class Meta:
        model = Teacher
        fields = (
            'user',
            'name',
            'second_name',
            'surname',
            'photo',
            'rang',
            'email',
            'diciplines'
        )