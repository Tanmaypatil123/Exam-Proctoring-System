from django.core.mail import EmailMessage
import os
import string
import random

class Util:
  @staticmethod
  def send_email(data):
    email = EmailMessage(
      subject=data['subject'],
      body=data['body'],
      from_email=os.environ.get('EMAIL_FROM'),
      to=[data['to_email']]
    )
    email.send()

def generate_random_password(length=6):
    letters = string.ascii_letters  # Includes uppercase and lowercase letters
    return ''.join(random.choice(letters) for _ in range(length))