from django import forms
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password',widget=forms.PasswordInput)

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


