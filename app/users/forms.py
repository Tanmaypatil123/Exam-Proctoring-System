from django import forms
from .models import Organization, Student
from django.contrib.auth.forms import UserCreationForm
from .models import StudentAuthentication


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ["name", "email", "password"]


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["organization", "name", "email", "exam"]


class StudentAuthenticationForm(UserCreationForm):
    class Meta:
        model = StudentAuthentication
        fields = ["username", "password"]  # Add relevant fields
