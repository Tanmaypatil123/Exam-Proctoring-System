from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from users.serializers import (
    SendPasswordResetEmailSerializer,
    UserChangePasswordSerializer,
    UserLoginSerializer,
    UserPasswordResetSerializer,
    UserProfileSerializer,
    UserRegistrationSerializer,
    StudentRegisterSerializer,
)
from django.contrib.auth import authenticate
from users.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from users.serializers import FeedbackSerializers
from users.utils import generate_random_password
from users.models import UserModel, Student
from users.serializers import StudentVerifySerializer
from exam.models import Exam
from django.core.mail import send_mail
from django.conf import settings

# Generate Token Manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_tokens_for_user(user)
        return Response(
            {"token": token, "msg": "Registration Successful"},
            status=status.HTTP_201_CREATED,
        )


class UserLoginView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get("email")
        password = serializer.data.get("password")
        user = authenticate(email=email, password=password)
        if user is not None:
            token = get_tokens_for_user(user)
            return Response(
                {"token": token, "msg": "Login Success"}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"errors": {"non_field_errors": ["Email or Password is not Valid"]}},
                status=status.HTTP_404_NOT_FOUND,
            )


class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = UserChangePasswordSerializer(
            data=request.data, context={"user": request.user}
        )
        serializer.is_valid(raise_exception=True)
        return Response(
            {"msg": "Password Changed Successfully"}, status=status.HTTP_200_OK
        )


class SendPasswordResetEmailView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            {"msg": "Password Reset link send. Please check your Email"},
            status=status.HTTP_200_OK,
        )


class UserPasswordResetView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, uid, token, format=None):
        serializer = UserPasswordResetSerializer(
            data=request.data, context={"uid": uid, "token": token}
        )
        serializer.is_valid(raise_exception=True)
        return Response(
            {"msg": "Password Reset Successfully"}, status=status.HTTP_200_OK
        )


class FeedBackAPIView(APIView):
    def post(self, request, format=None):
        serializer = FeedbackSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(
            {"msg": "Feedback recorded succesfully"}, status=status.HTTP_201_CREATED
        )


class StudentRegistrationAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = StudentRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = generate_random_password()
        organisation = request.user
        print(organisation)
        organisation = UserModel.objects.filter(email=organisation).first()
        print(organisation)
        print(request.data)
        exam = Exam.objects.filter(id=request.data.get("exam")).first()
        print(exam)
        student_data = {
            "organization": organisation,
            "name": request.data.get("name"),
            "email": request.data.get("email"),
            "exam": exam,
            "password": password,  # You might want to hash the password here
        }
        student = Student.objects.create(**student_data)
        subject = "Login credentials for your exam."
        message = f"""
            Login Id = {request.data.get("email")}
            Password = {password}
        """
        email_from = settings.EMAIL_HOST_USER
        recipien_list = [
            request.data.get("email"),
        ]

        send_mail( subject=subject,message =message,from_email= email_from,recipient_list=recipien_list)
        return Response(
            {
                "name": request.data.get("name"),
                "email": request.data.get("email"),
                "password": password,
            },
            status=status.HTTP_201_CREATED,
        )


class StudentVerifyAPIView(APIView):
    def post(self, request, format=None):
        serializer = StudentVerifySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        student = Student.objects.filter(email=request.data.get("email")).first()
        exam = student.exam
        if student is None:
            return Response(
                {"msg": "User is not registered"}, status=status.HTTP_404_NOT_FOUND
            )
        if student.password != request.data.get("password"):
            return Response(
                {"msg": "Password is incorrect"}, status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            {"msg": "Success", "exam_id": exam.id}, status=status.HTTP_200_OK
        )
