from django.db import models
from datetime import date

from semester.models import Semester
from program.models import Program, Department
# Create your models here.


class Teacher(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    techer_id = models.CharField(max_length=150)
    admited_semester = models.ForeignKey(
        Semester, on_delete=models.SET_NULL, null=True)
    date_of_birth = models.DateField(default=date.today)
    pn_number = models.IntegerField()
    email = models.EmailField(blank=True)
    addres = models.CharField(max_length=1000, blank=True)
    program = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now=True)
