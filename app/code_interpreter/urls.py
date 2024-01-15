from django.urls import path
from .views import CodingQuestionListCreate, TestCaseListCreate, SubmissionCreate

urlpatterns = [
    path("questions/", CodingQuestionListCreate.as_view(), name="question-list-create"),
    path("testcases/", TestCaseListCreate.as_view(), name="testcase-list-create"),
    path("submit/", SubmissionCreate.as_view(), name="submission-create"),
]
