from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

from main.models import Student, Teacher

User = get_user_model()

class LoginForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class EditStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('photo', )

class EditTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('email', 'photo',)
