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


def searchemp(request):
    name_query = request.GET.get("name")
    curr_grade_query = request.GET.get("currgrade")
    prev_grade_query = request.GET.get("prevgrade")

    # if you want get user from request
    # user = request.user.username

    students = None
    if (len(name_query) > 0) or (len(curr_grade_query) > 0) or (len(prev_grade_query) > 0):
        students = Student.objects.filter(
            Q(Student_name__icontains=name_query, Student_curr_grade__icontains=curr_grade_query,Student_prev_grade__icontains=prev_grade_query)).distinct()
    elif len(name_query) > 0:
        students = Student.objects.filter(Q(Student_name__icontains=name_query)).distinct()
    elif len(curr_grade_query) > 0:
        students = Student.objects.filter(Q(Student_curr_grade__icontains=curr_grade_query)).distinct()
    elif len(prev_grade_query) > 0:
        students = Student.objects.filter(Q(Student_prev_grade__icontains=prev_grade_query)).distinct()
    else:
        pass
    return render(request, 'home/emphome.html', {'students': students})


def searchment(request):
    name_query = request.GET.get("name")
    curr_grade_query = request.GET.get("currgrade")
    prev_grade_query = request.GET.get("prevgrade")

    # if you want get user from request
    # user = request.user.username

    students = None
    if (len(name_query) > 0) or (len(curr_grade_query) > 0) or (len(prev_grade_query) > 0):
        students = Student.objects.filter(
            Q(Student_name__icontains=name_query, Student_curr_grade__icontains=curr_grade_query,
              Student_prev_grade__icontains=prev_grade_query)).distinct()
    elif len(name_query) > 0:
        students = Student.objects.filter(Q(Student_name__icontains=name_query)).distinct()
    elif len(curr_grade_query) > 0:
        students = Student.objects.filter(Q(Student_curr_grade__icontains=curr_grade_query)).distinct()
    elif len(prev_grade_query) > 0:
        students = Student.objects.filter(Q(Student_prev_grade__icontains=prev_grade_query)).distinct()
    else:
        pass
    return render(request, 'home/mentorhome.html', {'students': students})

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
    students = Student.objects.filter(Emp_name__Employee_name=request.user.username)
    return render(request, 'home/emphome.html',
                  {'students': students})

def mentorhome(request):
    students = Student.objects.filter(Men_name__Mentor_name=request.user.username)
    return render(request, 'home/mentorhome.html',
                  {'students':students})

def markattendance(request):
    students = Student.objects.all()
    return render(request, 'home/markattendance.html',
                  {'students': students})

#def studentsreports(request):
#    return render(request, 'home/studentsreports.html',
#                  {'studentsreports': studentsreports})

def createappointments(request):
    return render(request, 'home/createappointments.html',
                  {'createappointments': createappointments})

def mentortask(request):
    return render(request, 'home/mentortask.html',
                  {'mentortask': mentortask})

def empmarkattendance(request):
    return render(request, 'home/empmarkattendance.html',
                  {'empmarkattendance': empmarkattendance})

#def empstudentsreports(request):
#    return render(request, 'home/empstudentsreports.html',
#                  {'empstudentsreports': empstudentsreports})

def empcreateappointments(request):
    return render(request, 'home/empcreateappointments.html',
                  {'empcreateappointments': empcreateappointments})

def emptask(request):
    return render(request, 'home/emptask.html',
                  {'emptask': emptask})

def mentstudlist(request):
    #users = request.user.username()
    students = Student.objects.filter(start_date__lte=timezone.now())
    return render(request, 'home/mentstudlist.html',
                  {'students': students})



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
                return emphome(request)
            else:
                login(request, user)
                return mentorhome(request)
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
    {'students': students})

def Student_Report(request):
    students = Student.objects.filter(start_date__lte=timezone.now())
    return render(request, 'home/studentsreports.html',
    {'students': students})

def Emp_Student_Report(request):
    students = Student.objects.filter(start_date__lte=timezone.now())
    return render(request, 'home/empstudentsreports.html',
    {'students': students})

def Student_Report_Edit(request,pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            student.updated_date = timezone.now()
            student.save()
            students = Student.objects.filter(start_date__lte=timezone.now())
            return render(request, 'home/studentsreports.html',
            {'students': students})
    else:
        form = StudentForm(instance=student)
        return render(request, 'home/studreportedit.html', {'form': form})


def Emp_Student_Report_Edit(request,pk):
    student = get_object_or_404(Student,pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            student.updated_date = timezone.now()
            student.save()
            students = Student.objects.filter(start_date__lte=timezone.now())
            return render(request, 'home/empstudentsreports.html',
            {'students': students})
    else:
        form = StudentForm(instance=student)
        return render(request, 'home/empstudreportedit.html', {'form': form})


def studentedit(request,pk):
   student = get_object_or_404(Student,pk=pk)
   if request.method == "POST":
       form = StudentForm(request.POST, instance=student)
       if form.is_valid():
           student = form.save()
           student.updated_date = timezone.now()
           student.save()
           students = Student.objects.filter(start_date__lte=timezone.now())
           return render(request, 'home/studentlist.html', {'students': students})
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
                          {'students': students})
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
           return render(request, 'home/studentlist.html', {'students': students})

    else:
           print("else")
     #  form = StudentForm(instance=student)
      # return render(request, 'home/studentsarchive.html', {'form': form})

def mentor_list(request):
    mentors = Mentor.objects.filter(begining_date__lte=timezone.now())
    return render(request, 'home/mentorlist.html',
                 {'mentors': mentors})


def mentor_edit(request, pk):
   mentor = get_object_or_404(Mentor, pk=pk)
   if request.method == "POST":
       form = MentorForm(request.POST, instance=mentor)
       if form.is_valid():
           mentor = form.save()
           mentor.updated_date = timezone.now()
           mentor.save()
           mentors = Mentor.objects.filter(begining_date__lte=timezone.now())
           return render(request, 'home/mentorlist.html', {'mentors': mentors})
   else:
       form = MentorForm(instance=mentor)
   return render(request, 'home/mentoredit.html', {'form': form})

def mentor_new(request):
    if request.method == "POST":
        form = MentorForm(request.POST)
        if form.is_valid():
            mentor = form.save(commit=False)
            mentor.start_date = timezone.now()
            mentor.save()
            mentors = Mentor.objects.filter(begining_date__lte=timezone.now())
            return render(request, 'home/mentorlist.html',
                          {'mentors': mentors})
    else:
        form = MentorForm()
        # print("Else")
    return render(request, 'home/mentornew.html', {'form': form})



