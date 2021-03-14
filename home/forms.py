
from django.contrib.auth.forms import UserCreationForm
from home.models import User
from django.core.validators import ValidationError
from django import forms

class SignUpForm(UserCreationForm):

   class Meta:
      model = User 
      fields = ('username', 'password1', 'password2',)