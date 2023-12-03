from app.models import *
from django import forms
class UserMOdelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password']
        widgets = {'password':forms.PasswordInput()}

class EMP(forms.ModelForm):
    class Meta:
        model = employee_data
        fields = ['name','email','mno','dob','age','profile_pic','address','Biodata']


        