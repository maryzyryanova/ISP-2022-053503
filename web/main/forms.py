from datetime import datetime
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.conf import settings

from main.models import Student, Teacher, Notification, Mark, Missings, Group

from main.utils import get_pairs


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
    def __init__(self, groups, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        tup = ((Group.objects.get(number=i['group__number']), i['group__number']) for i in groups.all())

        self.fields['group'] = forms.ChoiceField(
            choices=tup
        )

    class Meta:
            model = Notification
            fields = ('group', 'message')

class MarksForm(forms.Form):
    student = forms.ModelChoiceField(queryset=Student.objects.all())
    date = forms.ChoiceField(choices=((datetime.now().date(), 'df'),))
    mark = forms.IntegerField(required=False)
    missings = forms.IntegerField(required=False)

    def __init__(self, group, dicipline, *args, **kwargs):
        super(MarksForm, self).__init__(*args, **kwargs)

        dates = get_pairs(dicipline, group)
        
        res = ((i.date(), i.strftime("%d.%m")) for i in dates)

        self.fields['student'] = forms.ModelChoiceField(
            queryset=group.students.all()
        )

        self.fields['date'] = forms.ChoiceField(
            choices=res
        )
        