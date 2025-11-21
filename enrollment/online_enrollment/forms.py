from django import forms
from .models import Account, Student, School, Stud_fam, Address
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ["email", "password","name", "sex", "age"]

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "program","subject", "student_id", "ave_grade"]

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ["program", "subject","prof", "schedule", "ave_grade"]


class Stud_famForm(forms.ModelForm):
    class Meta:
        model = Stud_fam
        fields = ["guardian", "occupation","contact_no", "annual_inc", "citizenship"]

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["province", "municipality","brgy", "street", "postal"]

class RegisterForm (UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required= True, help_text ="Required! Enter a valid email address")

    class Meta:
        model = User
        fields = ['username', 'email','password1','password2' ]
            