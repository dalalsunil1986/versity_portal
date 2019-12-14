from django.db import models

from student.models import Student
from cource.models import Cource
from semester.models import Semester

# Create your models here.


class GradeSheet(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    cource = models.ForeignKey(Cource, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student
