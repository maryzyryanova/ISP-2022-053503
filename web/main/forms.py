from datetime import datetime
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.conf import settings

from main.models import Student, Teacher, Notification, Mark, Missings, Group

from main.utils import get_pairs
from main.models import ExamMark


User = get_user_model()

class LoginForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'

class EditStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('photo', )

    def __init__(self, *args, **kwargs):
        super(EditStudentForm, self).__init__(*args, **kwargs)
        self.fields['photo'].widget.attrs['class'] = 'form-control'    

class EditTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('email', 'photo',)

    def __init__(self, *args, **kwargs):
        super(EditTeacherForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['photo'].widget.attrs['class'] = 'form-control'

class MessageForm(forms.Form):
    message = forms.CharField()
    group = forms.ChoiceField(choices=Group.objects.all())

    def __init__(self, groups, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        tup = ((Group.objects.get(number=i['group__number']), i['group__number']) for i in groups.all())

        self.fields['group'] = forms.ChoiceField(
            choices=tup
        )

        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['group'].widget.attrs['class'] = 'form-select'

class MarksForm(forms.Form):
    student = forms.ModelChoiceField(queryset=Student.objects.all())
    date = forms.ChoiceField(choices=((datetime.now().date(), 'df'),))
    mark = forms.IntegerField(required=False)
    missings = forms.IntegerField(required=False)

    def __init__(self, group, dicipline, *args, **kwargs):
        super(MarksForm, self).__init__(*args, **kwargs)

        dates = get_pairs(dicipline, group)
        
        res = [(i.date(), i.strftime("%d.%m")) for i in dates]
        self.fields['student'] = forms.ModelChoiceField(
            queryset=group.students.all()
        )

        self.fields['date'] = forms.ChoiceField(
            choices=res
        )

        self.fields['mark'].widget.attrs['class'] = 'form-control'
        self.fields['missings'].widget.attrs['class'] = 'form-control'
        self.fields['student'].widget.attrs['class'] = 'form-select'
        self.fields['date'].widget.attrs['class'] = 'form-select'

class ExamMarksForm(forms.Form):
    mark = forms.IntegerField(required=False)
    student = forms.ModelChoiceField(queryset=Student.objects.all())
    
    def __init__(self, group, *args, **kwargs):
        super(ExamMarksForm, self).__init__(*args, **kwargs)

        self.fields['student'] = forms.ModelChoiceField(
            queryset=group.students.all()
        )

        self.fields['mark'].widget.attrs['class'] = 'form-control'
        self.fields['student'].widget.attrs['class'] = 'form-select'