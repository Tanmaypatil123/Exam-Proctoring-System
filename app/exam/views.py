from django.shortcuts import render
# from exam.forms import UserModelForm
from exam.serializers import ExamCreationSerializers,QuestionCreation,ResponseCreationSerializer,OptionCreationSerializer,WarningCreationSerializers,ExamDetailsSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response as RS
from rest_framework import status
from rest_framework.views import APIView
from users.renderers import UserRenderer
from exam.models import *
# Create your views here.

def home(request):
    return render(request,"exam/index.html")

class GetExamDetailes(APIView):
    def get(self,request,format = None):
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
            data['queations'] = {}
            # Iterate over questions and options
            for que in exam.queation:
                data['queations'][str(que.id)] = {'title': str(que.question), 'options': []}
                for opt in que.options:
                    data['queations'][str(que.id)]['options'].append(str(opt.options))

        return RS(data=data,status=status.HTTP_200_OK)


class ExamAPIView(APIView):
    permission_classes = [
        IsAuthenticated
    ]

    renderer_classes = [
        UserRenderer
    ]

    def post(self,request,format=None):
        serializer = ExamCreationSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user
        # token = get_tokens_for_user(user)
        exam = serializer.save(organisation=user)
        return RS({'exam':str(exam.id), 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)
    
class QuestionAPIView(APIView):
    permission_classes = [
        IsAuthenticated
    ]

    renderer_classes = [
        UserRenderer
    ]

    def post(self,request,format=None):
        serializer = QuestionCreation(data=request.data)
        if serializer.is_valid():
            print(serializer)
            exam = Exam.objects.filter(id = serializer.data.get("exam_id")).first()
            question = Questions.objects.create(
                exam = exam,
                question = serializer.data.get("question")
            )
            return RS({
                "msg": "question creted succesfully"
            },status=status.HTTP_201_CREATED)
        
class OptionCreationAPIView(APIView):

    permission_classes = [
        IsAuthenticated
    ]
    renderer_classes = [
        UserRenderer
    ]

    def post(self,request,format = None):
        serializer = OptionCreationSerializer(data=request.data)
        if serializer.is_valid():
            question = Questions.objects.filter(id = serializer.data.get("question_id")).first()
            option = AnswerOptions.objects.create(
                options = serializer.data.get("option"),
                question = question
            )
        return RS({
            "Option created " : f"{serializer.data.get('option')}",
            "question_id" : f"{serializer.data.get('question_id')}"
        },status=status.HTTP_201_CREATED)

class ResponseCreationAPIView(APIView):
    permission_classes = [
        IsAuthenticated
    ]

    renderer_classes = [
        UserRenderer
    ]

    def post(self,request,format=None):
        serializer = ResponseCreationSerializer(data=request.data)
        if serializer.is_valid():
            option = AnswerOptions.objects.filter(serializer.data.get("option_id")).first()
            student = request.user 

            response = Response.objects.create(
                Response = option,
                student = student
            )
        return RS({
            "msg" : "Response Recorded"
        },status=status.HTTP_201_CREATED)
    
class WarningAPIView(APIView):
    permission_classes = [
        IsAuthenticated
    ]
    renderer_classes = [
        UserRenderer
    ]

    def post(self, request,format = None):
        serialilzer = WarningCreationSerializers(data=request.data)
        if serialilzer.is_valid():
            student = request.user
            warning = Warning.objects.create(
                message = serialilzer.data.get("message"),
                student = student
            )
        ## Remained to write logic for count increment and disqalification .
        return RS({
            "msg" : "Warning recorded Recorded."
        },status=status.HTTP_201_CREATED)
