from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=100, required=True)
    phone = forms.CharField(max_length=100,required=True)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    age = forms.IntegerField(required=False)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'age', 'gender', 'password1', 'password2')
