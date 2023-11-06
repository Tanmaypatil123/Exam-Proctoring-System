from django.urls import path 
from management.views import upload_students_details
urlpatterns = [
    path('upload-studnets-data/',upload_students_details,name='upload_student_data')
]
