from django.db import models
import uuid
from users.models import UserModel, Student

# Create your models here.


class Exam(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=100, blank=False, null=False)

    description = models.CharField(max_length=500, blank=False, null=False)

    no_of_questions = models.IntegerField(blank=False, null=False)

    duration = models.IntegerField(blank=False, null=False, default=60)

    max_warning_limit = models.IntegerField(blank=False, null=False, default=15)
    organisation = models.ForeignKey(to=UserModel, on_delete=models.CASCADE)

    @property
    def queation(self):
        return Questions.objects.filter(exam=self)


class Questions(models.Model):
    exam = models.ForeignKey(to=Exam, on_delete=models.CASCADE)
    question = models.CharField(max_length=1000, null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    @property
    def options(self):
        return AnswerOptions.objects.filter(question=self)


class AnswerOptions(models.Model):
    options = models.CharField(max_length=100, null=False, blank=False)

    question = models.ForeignKey(to=Questions, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


##  Add models for responses
class Response(models.Model):
    Response = models.ForeignKey(to=AnswerOptions, on_delete=models.CASCADE)
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE)


class Warning(models.Model):
    message = models.CharField(max_length=200, blank=False, null=False)
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE)


class Warning_count(models.Model):
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE)
    count = models.IntegerField(default=0, blank=False, null=False)


## Add models for warning
## Add models for sessions
