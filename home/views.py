from django.shortcuts import render

# Create your views here.


from django.http import JsonResponse
from django.utils import timezone
from .models import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.db.models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.db.models import Q
from .models import Student,Mentor,Employee
from .forms import StudentForm,UserForm,EmployeeForm


def search(request):
    students = Student.objects.values('Student_name', 'Student_grade', 'School')
    query = request.GET.get("q")
    if query:
        students = students.filter(
            Q(Student_name__icontains=query)
        ).distinct()
        return render(request, 'home/emphome.html', {
            'students': students,
        })
    else:
        return render(request, 'home/emphome.html', {'students': students})

def home(request):
    return render(request, 'home/base.html',
                  {'home': home})

def about(request):
    return render(request, 'home/about.html',
                  {'about': about})


def mentor(request):
    return render(request, 'home/mentor.html',
                  {'mentor': mentor})

def index(request):
    return render(request, 'home/index.html',
                  {'index': index})

def empindex(request):
    return render(request, 'home/empindex.html',
                  {'empindex': empindex})

def emphome(request):
    students = Student.objects.filter(start_date__lte=timezone.now())
    return render(request, 'home/emphome.html',
                  {'home': students})

def mentorhome(request):
    return render(request, 'home/mentorhome.html',
                  {'mentorhome': mentorhome})

def markattendance(request):
    return render(request, 'home/markattendance.html',
                  {'markattendance': markattendance})

def studentsreports(request):
    return render(request, 'home/studentsreports.html',
                  {'studentsreports': studentsreports})

def createappointments(request):
    return render(request, 'home/createappointments.html',
                  {'createappointments': createappointments})

def mentortask(request):
    return render(request, 'home/mentortask.html',
                  {'mentortask': mentortask})

def empmarkattendance(request):
    return render(request, 'home/empmarkattendance.html',
                  {'empmarkattendance': empmarkattendance})

def empstudentsreports(request):
    return render(request, 'home/empstudentsreports.html',
                  {'empstudentsreports': empstudentsreports})

def empcreateappointments(request):
    return render(request, 'home/empcreateappointments.html',
                  {'empcreateappointments': empcreateappointments})

def emptask(request):
    return render(request, 'home/emptask.html',
                  {'emptask': emptask})



def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'home/base.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_staff:
                login(request, user)
                return render(request, 'home/emphome.html')
            else:
                login(request, user)
                return render(request, 'home/mentorhome.html')
        else:
            return render(request, 'home/login.html', {'error_message': 'Invalid login'})
    return render(request, 'home/login.html')

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'home/login.html')
    context = {
        "form": form,
    }
    return render(request, 'home/register.html', context)

def password_reset(request):
    return render(request, 'home/password_reset.html',
    {'home': password_reset})


def password_reset_confirm(request):
    return render(request, 'home/password_reset_confirm.html',
    {'home': password_reset_confirm})

def password_reset_email(request):
    return render(request, 'home/password_reset_email.html',
    {'home': password_reset_email})

def password_reset_complete(request):
    return render(request, 'home/password_reset_complete.html',
    {'home': password_reset_complete})

def Student_list(request):
    students = Student.objects.filter(start_date__lte=timezone.now())
    return render(request, 'home/studentlist.html',
    {'home': students})


def studentedit(request,pk):
   student = get_object_or_404(Student,pk=pk)
   if request.method == "POST":
       form = StudentForm(request.POST, instance=student)
       if form.is_valid():
           student = form.save()
           # stock.customer = stock.id
           student.updated_date = timezone.now()
           student.save()
           students = Student.objects.filter(start_date__lte=timezone.now())
           return render(request, 'home/studentlist.html', {'student': students})
   else:
       # print("else")
       form = StudentForm(instance=student)
   return render(request, 'home/studentedit.html', {'form': form})

def studentadd(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.start_date = timezone.now()
            student.save()
            students = Student.objects.filter(start_date__lte=timezone.now())
            return render(request, 'home/studentlist.html',
                          {'student': students})
    else:
        form = StudentForm()
        # print("Else")
    return render(request, 'home/studentadd.html', {'form': form})



def studentsarchive(request):
    student = get_object_or_404(Student)
    if request.method =="POST":
       form = StudentForm(request.POST, instance = student)
       print("one")
       if form.is_valid():
           print("2")
           student= form.save()
           print("3")
           Stud_id = form.cleaned_data['Student ID']
           print("4")
           student_arch= Student.object.filter(Student_id = Stud_id)
           print("5")
           student_arch.delete()
           students = StudentForm(instance=student)
           return render(request, 'home/studentlist.html', {'student': students})

    else:
           print("else")
     #  form = StudentForm(instance=student)
      # return render(request, 'home/studentsarchive.html', {'form': form})

def mentor_list(request):
    mentor_list = Mentor.objects.filter(begining_date__lte=timezone.now())
    return render(request, 'home/mentorlist.html',
                 {'home': mentor_list})



def mentor_edit(request, pk):
   mentor = get_object_or_404(Mentor, pk=pk)
   if request.method == "POST":
       form = MentorForm(request.POST, instance=mentor)
       if form.is_valid():
           mentor = form.save()
           # stock.customer = stock.id
           mentor.updated_date = timezone.now()
           mentor.save()
           mentors = Mentor.objects.filter(begining_date__lte=timezone.now())
           return render(request, 'home/mentorlist.html', {'mentors': mentors})
   else:
       # print("else")
       form = MentorForm(instance=mentor)
   return render(request, 'home/mentoredit.html', {'form': form})
