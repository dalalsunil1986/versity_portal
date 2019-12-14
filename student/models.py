from django.db import models
from datetime import date

from semester.models import Semester
from teacher.models import Teacher
from program.models import Program, Department

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250, blank=True)
    std_id = models.CharField(max_length=100)
    admited_semester = models.ForeignKey(
        Semester, on_delete=models.SET_NULL, null=True)
    date_of_birth = models.DateField(default=date.today)
    pn_number = models.IntegerField()
    email = models.EmailField()
    addres = models.CharField(max_length=1000)
    advisor = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    program = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True)
    is_graduate = models.BooleanField(default=False)
    cgpa = models.DecimalField(
        max_digits=2, decimal_places=2, default=0.0, blank=True)
    date = models.DateTimeField(auto_now=True)
