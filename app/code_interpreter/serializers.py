from rest_framework import serializers
from .models import CodingQuestion, TestCase, Submission


class TestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCase
        fields = ["input", "output"]


class CodingQuestionSerializer(serializers.ModelSerializer):
    testcases = TestCaseSerializer(many=True, read_only=True)

    class Meta:
        model = CodingQuestion
        fields = ["id", "title", "description", "language", "testcases", "exam"]


class SubmissionSerializer(serializers.Serializer):
    class Meta:
        # model = Submission
        fields = ["question_id", "code"]
