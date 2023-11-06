from django.db import models

class StudentData(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    passing_year = models.IntegerField()

    def __str__(self):
        return self.first_name  # Change this to something meaningful

class DemoFile(models.Model):
    file = models.FileField(upload_to='demofile',default=None)
    is_active = models.BooleanField(default=True)