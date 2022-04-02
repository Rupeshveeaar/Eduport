from dataclasses import field
from django import forms
from studentapp.models import Course , CustomUser

from django.forms.fields import DateField
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import( PasswordChangeForm, UserCreationForm , 
UserChangeForm ,AuthenticationForm ,SetPasswordForm, UsernameField , PasswordResetForm)
from django.forms import TextInput, fields , EmailInput, widgets
from django.contrib.auth import password_validation
from django.utils.translation import gettext , gettext_lazy as _
from .models import*
from django.core.exceptions import ValidationError


# class Form_data(forms.ModelForm):
#     class Meta:
#         model=Course
#         fields=['profile_course_pic','name' ,'instructor_name', 'course_price']
#         widgets={
#             'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter The Course Name', 'required':'required'}),
#             'instructor_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter The Instructor Name', 'required':'required'}),
#             'course_price':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Enter The Amount', 'required':'required'}),
#         }



class RegistrationFormUser(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password' , 'class':'form-control','placeholder':'Enter the  Password '}),
        help_text=password_validation.password_validators_help_text_html(),
        )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password' , 'class':'form-control' , 'placeholder':'Confirm Password Again'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
        )
    class Meta:
        model=CustomUser
        fields=('username' , 'email')
        labels={'email':'Email'}
       
        widgets = {
        'username':TextInput(attrs={'class':'form-control','placeholder':'Enter the Username','required':'required'}),
        'email':EmailInput(attrs={'class':'form-control', 'placeholder':'Enter the Email', 'required':'required'}),

        
        }
