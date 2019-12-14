from django.db import models

bulding_list = (('main', 'Main'), ('ab1', "AB1"), ('ab2', "AB2"))
# Create your models here.


class Bulding(models.Model):
    name = models.CharField(
        max_length=50, choices=bulding_list, default='main')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
