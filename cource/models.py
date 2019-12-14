from django.db import models
from datetime import time, datetime
from program.models import Department
from teacher.models import Teacher
from pages.models import Bulding

# Create your models here.

credits_list = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('4.5', "4.5"))
days = (('S', 'Sunday'), ('M', "Monday"), ('T', "Tuesday"),
        ('W', "Wednesday"), ('R', "Thursday"))
class_durations = (('1.20', "1.20"), ("2", "2"), ('3', "3"))


class Cource (models.Model):
    name = models.CharField(max_length=250)
    short_name = models.CharField(max_length=50)
    credit = models.IntegerField(choices=credits_list, default='3')
    require_credit = models.IntegerField(default=0)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    for_all = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Section (models.Model):
    number = models.IntegerField(default=1)
    cource = models.ForeignKey(Cource, on_delete=models.CASCADE)
    instructor = models.ForeignKey(
        Teacher, on_delete=models.SET_NULL, null=True)
    capacity = models.IntegerField(default=40)
    taken = models.IntegerField(default=0)
    fill = models.BooleanField(default=False)
    lab = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.number


class Classes (models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    day = models.CharField(max_length=30, choices=days, default="S")
    start = models.TimeField(default=time)
    duration = models.CharField(
        choices=class_durations, default='1.20', max_length=10)
    end = models.TimeField(default=time)
    room_number = models.IntegerField()
    bulding = models.ForeignKey(
        Bulding, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.room_number


class CourceLab(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    day = models.CharField(max_length=30, choices=days, default="S")
    start = models.TimeField(default=time)
    duration = models.CharField(
        choices=class_durations, default='1.20', max_length=10)
    end = models.TimeField(default=time)
    room_number = models.IntegerField()
    bulding = models.ForeignKey(
        Bulding, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.room_number
