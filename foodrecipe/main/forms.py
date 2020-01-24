from django import forms
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class RegistrationForm(forms.ModelForm):

    email = forms.CharField(label='Email Address', widget=forms.TextInput(

        attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email address..',
            
        }
    ))
   
    username = forms.CharField(widget=forms.TextInput(

        attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username...'
        }
    ))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter a password...'
        }
    ))
    password2 = forms.CharField(label='Confirm password',widget=forms.PasswordInput(
         attrs={
            'class': 'form-control',
            'placeholder': 'Re-enter your password...'
        }
    ))

    class Meta:
        model = User
        fields = ('email','username')

    def clean_email(self):
        email= self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email is already taken")
        return email

    def clean_password2(self):
        # check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password is not matched")
        return password2    


