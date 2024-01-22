from django import forms
from django.forms import ModelForm, Widget
from .models import acc


# class NameForm(forms.Form):
#     firstName = forms.CharField(max_length=30, label = "First Name")
#     lastName = forms.CharField(max_length =30, label = "Last Name")
#     username = forms.CharField(max_length = 30, label = "username")
#     password = forms.CharField(widget=forms.PasswordInput())
#     confirmPassword = forms.CharField(widget=forms.PasswordInput())
#     profilePhoto = forms.FileField()
#     dob = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
#     email = forms.EmailField()

class AccForm(ModelForm):
    class Meta:
        model = acc
        fields = "__all__"

        labels = {
            "fname": "First Name",
            "lname": "Last Name",
            "username": "Username",
            "dob": "Date of Birth",
            "email": "Email",
            "photo": "Profile Photo"
        }

        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'})
        }
