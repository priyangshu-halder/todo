from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model=Task
        fields=[
            'unique_id',
            'task',
        ]

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=[
            'username',
            'email',
            'password1',
            'password2',
        ]
        