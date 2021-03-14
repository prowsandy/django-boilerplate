
from django.contrib.auth.forms import UserCreationForm
from home.models import User
from django.core.validators import ValidationError
from django import forms

class SignUpForm(UserCreationForm):
   email = forms.EmailField(required=True,label='Email',error_messages={'exists': 'Oops! Email already exist'})
   class Meta:
      model = User 
      fields = ('username', 'email', 'password1', 'password2',)

   def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

   def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise ValidationError(self.fields['email'].error_messages['exists'])
        return self.cleaned_data['email']