from django.urls import path
from exam.views import (
    ExamAPIView,
    QuestionAPIView,
    ResponseCreationAPIView,
    OptionCreationAPIView,
    WarningAPIView,
    GetExamDetailes,
)

urlpatterns = [
    path("create-exam/", ExamAPIView.as_view(), name="exam creation"),
    path("options/", OptionCreationAPIView.as_view(), name="option creation"),
    path("warning/", WarningAPIView.as_view(), name="warning message"),
    path("question/", QuestionAPIView.as_view(), name="question creation"),
    path("response/", ResponseCreationAPIView.as_view(), name="response creation"),
    path("get-exam-deails/", GetExamDetailes.as_view()),
]
