from rest_framework import serializers
from exam.models import *

class ExamDetailsSerializers(serializers.Serializer):
    exam_id = serializers.CharField()

class ExamCreationSerializers(serializers.ModelSerializer):
    class Meta :
        model = Exam
        fields = [
            "name","description","no_of_questions","max_warning_limit"
        ]

class QuestionCreation(serializers.Serializer):
    exam_id = serializers.CharField()
    question = serializers.CharField()
    
    class Meta :
        
        fields = [
            "question","exam_id"
        ]

class OptionCreationSerializer(serializers.Serializer):
    question_id = serializers.CharField()
    option = serializers.CharField()
    
    class Meta :
        
        fields = [
            "option","question_id"
        ]

class ResponseCreationSerializer(serializers.Serializer):
    response = models.CharField()
    
    class Meta :
        fields = [
            "option_id"
        ]

class WarningCreationSerializers(serializers.Serializer):
    message = models.CharField()

    class Meta:
        fields = [
            "message"
        ]
