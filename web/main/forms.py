from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()

# class LoginForm(forms.Form):
    # username = forms.CharField()
    # password = forms.CharField(widget=forms.PasswordInput)

class LoginForm(AuthenticationForm, forms.ModelForm):
    '''
        Authorization User Form
    '''

    class Meta:
        model = User
        fields = ('username', 'password')