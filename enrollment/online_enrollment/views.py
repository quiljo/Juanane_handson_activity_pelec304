from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Account, Student, School, Stud_fam, Address
from .forms import RegisterForm

from django.contrib.auth.decorators import login_required

def account_view(request):
    form = Account.objects.all()
    return render(request, 'student_acc.html', {'form': form} )

def student_view(request):
    form = Student.objects.all()
    return render(request, 'student.html', {'form': form} )


def school_view(request):
    form = School.objects.all()
    return render(request, 'school.html', {'form': form} )


def studfam_view(request):
    form = Stud_fam.objects.all()
    return render(request, 'stud_fam.html', {'form': form} )

def address_view(request):
    form = Address.objects.all()
    return render(request, 'address.html', {'form': form} )

def success(request):
    return render(request, 'success.html')

# ACCOUNT

def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login_user')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid input.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login_user')

@login_required(login_url='login_user')
def dashboard(request):
    return render(request, 'dashboard.html')