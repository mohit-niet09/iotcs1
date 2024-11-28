from django.shortcuts import render, redirect
from academic.models import Student
from academic.forms import *
from academic.utils import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def create_student(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('stdName')
        age = data.get('stdAge')
        email = data.get('stdEmail')
        Student.objects.create(name=name, age=age, email=email)
        return redirect('/create-student')
    return render(request, 'create-student.html')

@login_required(login_url='/login')
def get_students(request):
    students = Student.objects.values()
    return render(request, 'students.html', context={'test':students})

def delete_student(request, id):
    data = Student.objects.get(id=id)
    data.delete()
    return redirect('/students')
    
    
def update_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        updated_data = request.POST
        student.name = updated_data.get('stdName')
        student.age = updated_data.get('stdAge')
        student.email = updated_data.get('stdEmail')
        student.save()
        return redirect('/students')
    return render(request, 'update-student.html', context={'data':student})

def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            age = form.cleaned_data.get('age')
            Student.objects.create(name=name, age=age, email=email)
            redirect('/create')
    form = StudentForm()
    return render(request, 'createstd.html', context={'test':form})

def employee_form(request):
    form = EmployeeForm()
    return render(request, 'employee.html', context={'test':form})

def send_email_demo(request):
    if request.method == 'POST':
        reclist = []
        data = request.POST
        subject = data.get('subject')
        email = data.get('email')
        reclist.append(email)
        body = data.get('body')
        send_email_util(subject, body, reclist)
        return redirect('/sendemail')
    return render(request, 'test.html')

def register_user(request):
    if request.method == 'POST':
        data = request.POST
        first_name = data.get('fname')
        last_name = data.get('lname')
        email = data.get('uemail')
        user_name = data.get('username')
        password = data.get('password')
        user = User(first_name=first_name, last_name=last_name, email=email, username=user_name)
        user.set_password(password)
        user.save()
        return redirect('/register')
    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'invalid user name')
            return redirect('/login')
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, 'invalid password')
            return redirect('/login')
        else:
            login(request, user)
            return redirect('/students') 
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('/login')