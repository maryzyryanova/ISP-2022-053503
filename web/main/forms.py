from urllib import request
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.conf import settings

from main.models import Student, Teacher, Notification, Schedule, Mark

from datetime import datetime, timedelta


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

class MessageForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['group', 'message']

class MarksForm(forms.ModelForm):
    def __init__(self, student, dicipline, *args, **kwargs):
        super(MarksForm, self).__init__(*args, **kwargs)

        pairs = Schedule.objects.filter(dicipline=dicipline, group=student.group).order_by('week','day','bell')
        time = settings.SEMESTER_BEGIN
        dates = []
        count = 0
        i = 0
        while True:
            if i==pairs.count():
                i = 0
                count+=1
            pair = pairs[i]
            new_date = timedelta(days=7*pair.week*4*count+pair.day+1) + settings.SEMESTER_BEGIN
            time=new_date
            if time<settings.SEMESTER_END:
                dates.append(new_date)
                i+=1
            else:
                break
        
        res = ((i, i.strftime("%d.%m")) for i in dates)

        self.fields['date'] = forms.ChoiceField(
            choices=res
        )
        self.fields['student'].initial = student
        # self.fields['schedule'] = forms.ModelChoiceField(
        #     queryset=Schedule.objects.filter(group=student.group, dicipline = dicipline)
        # )
        
    class Meta:
        model = Mark
        fields = '__all__'
        # exclude = ('student',)