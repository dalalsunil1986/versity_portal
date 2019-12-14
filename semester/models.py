from django.db import models

# Create your models here.
semester_choice = (("Fall", "Fall"), ("Spring", "Spring"),
                   ("Summer", "Summer"))


class Semester(models.Model):
    title = models.CharField(max_length=200)
    season = models.CharField(
        max_length=150, choices=semester_choice, default="Fall")
    year = models.IntegerField()

    def get_title(self):
        title = f"{self.season} {self.year}"
        title.save()

    def __str__(self):
        return self.title
