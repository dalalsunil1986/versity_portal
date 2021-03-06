from django.db import models

# Create your models here.


class Program(models.Model):
    short_name = models.CharField(max_length=50)
    name = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    short_name = models.CharField(max_length=50)
    name = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
