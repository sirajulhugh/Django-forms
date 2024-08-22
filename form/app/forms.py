from django import forms
from app.models import Employee

class Employeeforms(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'