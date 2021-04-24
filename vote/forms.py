from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import forms
from vote.models import Candidate, Vote
from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2'
        ]


class UserTestForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = [
            'User'
        ]
