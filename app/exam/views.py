from django.shortcuts import render

# from exam.forms import UserModelForm
from exam.serializers import (
    ExamCreationSerializers,
    QuestionCreation,
    ResponseCreationSerializer,
    OptionCreationSerializer,
    WarningCreationSerializers,
    ExamDetailsSerializers,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response as RS
from rest_framework import status
from rest_framework.views import APIView
from users.renderers import UserRenderer
from exam.models import *
from code_interpreter.models import *

# Create your views here.


def home(request):
    return render(request, "exam/index.html")


class GetExamDetailes(APIView):
    def get(self, request, format=None):
        # get exam from exam details or exam id
        data = {}
        data["exam"] = {}  # Initialize as a dictionary
        serializer = ExamDetailsSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            exam = Exam.objects.filter(id=serializer.data.get("exam_id")).first()
            print(f"## {serializer.data.get('exam_id')} {exam}")

            # Assign values to data["exam"]
            data["exam"]["name"] = str(exam.name)
            data["exam"]["id"] = str(exam.id)
            data["exam"]["description"] = str(exam.description)
            data["exam"]["no_of_questions"] = str(exam.no_of_questions)
            data["exam"]["max_warning_limit"] = str(exam.max_warning_limit)
            data["exam"]["organisation"] = str(exam.organisation)
            data["exam"]["duration"] = exam.duration
            data["queations"] = {}
            # Iterate over questions and options
            for que in exam.queation:
                data["queations"][str(que.id)] = {
                    "title": str(que.question),
                    "options": [],
                    "options_id": [],
                }
                for opt in que.options:
                    data["queations"][str(que.id)]["options"].append(str(opt.options))
                    data["queations"][str(que.id)]["options_id"].append(str(opt.id))

            data["coding_questions"] = {}
            coding_questions = CodingQuestion.objects.filter(exam=exam).all()
            for ques in coding_questions:
                data["coding_questions"][str(ques.id)] = {
                    "title": str(ques.title),
                    "description": str(ques.description),
                    "testcases": {},
                }
                testcases = TestCase.objects.filter(question=ques).all()
                print(testcases)
                print(len(testcases))
                if len(testcases) >= 1:
                    for i in testcases:
                        pre = {"input": i.input, "output": i.output}
                        data["coding_questions"][str(ques.id)]["testcases"][
                            str(i.id)
                        ] = pre

                # data["coding_questions"][str(ques.id)]["question"].append

        return RS(data=data, status=status.HTTP_200_OK)


class ExamAPIView(APIView):
    permission_classes = [IsAuthenticated]

    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = ExamCreationSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user
        # token = get_tokens_for_user(user)
        exam = serializer.save(organisation=user)
        return RS(
            {"exam": str(exam.id), "msg": "Registration Successful"},
            status=status.HTTP_201_CREATED,
        )


class QuestionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        # create question for an exam
        serializer = QuestionCreation(data=request.data)
        if serializer.is_valid(raise_exception=True):
            exam_id = serializer.validated_data["exam_id"]
            question_text = serializer.validated_data["question"]

            exam = Exam.objects.get(id=exam_id)

            # Create a new question associated with the exam
            question = Questions.objects.create(exam=exam, question=question_text)

            return RS(
                data={"question_id": str(question.id)}, status=status.HTTP_201_CREATED
            )

        return RS(data={}, status=status.HTTP_400_BAD_REQUEST)


class OptionCreationAPIView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = OptionCreationSerializer(data=request.data)
        if serializer.is_valid():
            question = Questions.objects.filter(
                id=serializer.data.get("question_id")
            ).first()
            option = AnswerOptions.objects.create(
                options=serializer.data.get("option"), question=question
            )
        return RS(
            {
                "Option created ": f"{serializer.data.get('option')}",
                "question_id": f"{serializer.data.get('question_id')}",
            },
            status=status.HTTP_201_CREATED,
        )


class ResponseCreationAPIView(APIView):
    permission_classes = [IsAuthenticated]

    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = ResponseCreationSerializer(data=request.data)
        if serializer.is_valid():
            option = AnswerOptions.objects.filter(
                serializer.data.get("option_id")
            ).first()
            # student = request.user
            student = Student.objects.filter(email=serializer.data.get("student_email"))
            print(student)
            response = Response.objects.create(Response=option, student=student)
        return RS({"msg": "Response Recorded"}, status=status.HTTP_201_CREATED)


class WarningAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serialilzer = WarningCreationSerializers(data=request.data)
        if serialilzer.is_valid():
            # student = request.user
            print(request.data)
            student = Student.objects.filter(email = request.data["email"]).first()
            print(student)
            warning = Warning.objects.create(
                message=request.data["message"], student=student
            )
        ## Remained to write logic for count increment and disqalification .
        return RS({"msg": "Warning recorded Recorded."}, status=status.HTTP_201_CREATED)
