from django import forms
from .models import Employee



class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ["full_name", "username", "address", "email", "phone_number", "salary", "is_married", "position"]


# class EmployeeForm(forms.Form):
#     full_name = forms.CharField(max_length=255)
#     username = forms.CharField(max_length=255)
#     address = forms.CharField(max_length=255)
#     email = forms.EmailField()
#     phone_number = forms.CharField(max_length=255)
#     salary = forms.FloatField()
#     is_married = forms.BooleanField()
#     department = forms.IntegerField()