from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.core.mail import EmailMessage
# Create your views here.

class SendMailAPI(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        def post(self, request, format=None):
            user = request.user.email
            subject = request.data.get('subject')
            message = request.data.get('subject')
            from_email = 'ourmail@gmail.com'
            recipient_list = [user]
            # send mail
            email = EmailMessage(subject, message, from_email, recipient_list)
            # email.attach_file('path_to_attachment.pdf')  # Replace with the path to your attachment file
            email.send()
