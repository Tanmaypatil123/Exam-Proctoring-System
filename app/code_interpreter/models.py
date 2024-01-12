from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import uuid

class CodingQuestion(models.Model):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False) 
    title = models.CharField(max_length=100)
    description = models.TextField()
    language = models.CharField(max_length=50, default='Python')
    exam = models.ForeignKey(to = "exam.Exam",on_delete = models.CASCADE)

class TestCase(models.Model):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False) 
    question = models.ForeignKey(CodingQuestion, on_delete=models.CASCADE)
    input = models.TextField()
    output = models.TextField()


class Submission(models.Model):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False) 
    question = models.ForeignKey(CodingQuestion, on_delete=models.CASCADE)
    code = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)