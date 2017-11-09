from django.contrib import admin
from .models import Employee, Mentor, Student




class EmployeeList(admin.ModelAdmin):
    list_display = ('Employee_name', 'Employee_phone', 'Employee_Address', 'Employee_Id')
    search_fields = ('Employee_name', 'Employee_phone','Employee_Id')


class MentorList(admin.ModelAdmin):
    list_display = ('Mentor_name', 'Mentor_phone', 'Mentor_Id','Mentor_Address','Mentor_Gender','begining_date','ending_date')
    search_fields = ('Mentor_name', 'Mentor_phone','Mentor_Id','begining_date','ending_date')

class StudentList(admin.ModelAdmin):
    list_display = ('Student_id', 'Student_name', 'Student_email', 'Student_grade','Parents_email',
                    'Parents_phone', 'School', 'Men_name','Emp_name','start_date','last_date')
    search_fields = ('Student_name', 'Student_id', 'School' ,'Parents_phone','start_date','last_date',)

admin.site.register(Employee,EmployeeList )
admin.site.register(Mentor,MentorList)
admin.site.register(Student, StudentList)