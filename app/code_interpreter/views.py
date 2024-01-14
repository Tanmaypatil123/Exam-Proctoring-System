from rest_framework import generics
from .models import CodingQuestion, TestCase
from rest_framework import status
from rest_framework.response import Response
import traceback
import sys
from io import StringIO
from contextlib import redirect_stdout
import autopep8
from .serializers import CodingQuestionSerializer, TestCaseSerializer,SubmissionSerializer
from exam.models import Exam

class CodingQuestionListCreate(generics.ListCreateAPIView):
    queryset = CodingQuestion.objects.all()
    serializer_class = CodingQuestionSerializer

    def perform_create(self, serializer):
        coding_question_instance = serializer.save()
        test_cases_data = self.request.data.get('testcases', [])

        print(test_cases_data)
        for test_case_data in test_cases_data:
            TestCase.objects.create(
                question=coding_question_instance,
                input=test_case_data.get('input'),
                output=test_case_data.get('output'),
            )

class TestCaseListCreate(generics.ListCreateAPIView):
    queryset = TestCase.objects.all()
    serializer_class = TestCaseSerializer

class SubmissionCreate(generics.CreateAPIView):
    serializer_class = SubmissionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        code = request.data.get("code")

        # print(request.data.get("code"))
        # print(request.data.get("question_id"))
        # print(request.user)

        question = CodingQuestion.objects.filter(id = request.data.get("question_id")).first()
        
      
        passed_test_cases, failed_test_cases = self.evaluate_submission(question,code)
        print(passed_test_cases)
        print(failed_test_cases)
        # return Response({
        #     "msg" : "hey reache till here ."
        # },status=status.HTTP_200_OK)
        return Response({
            'passed': len(passed_test_cases),
            'failed': len(failed_test_cases),
            'failed_details' : failed_test_cases
            
        }, status=status.HTTP_201_CREATED)
    

    def evaluate_submission(self, question, code):
        test_cases = TestCase.objects.filter(question=question)
        passed_test_cases = []
        failed_test_cases = []
        code_template = """
        {input_data}

        {code}
        """
        for test_case in test_cases:
            input_data = test_case.input
            expected_output = test_case.output

            execution_data = {
                'input_data': input_data,
                'output_data': None  
            }
            code_to_exe = code_template.format(
                input_data = input_data,
                code = code
            )
            code_to_exe = autopep8.fix_code(code_to_exe)
            try:
                f = StringIO()
                with redirect_stdout(f):
                    exec(code_to_exe, {}, execution_data)
                s = f.getvalue()
                s = s.rstrip("\n")
                # print(f"I ma printing s {s}")
                execution_data['output_data'] = s
            except Exception as e:
            
                traceback_msg = traceback.format_exc()
                failed_test_cases.append({
                    'input': input_data,
                    'expected_output': expected_output,
                    'error': traceback_msg
                })
                continue
            print(execution_data)
            actual_output = execution_data['output_data']
            if actual_output == expected_output:
                passed_test_cases.append({
                    'input': input_data,
                    'expected_output': expected_output
                })
            else:
                failed_test_cases.append({
                    'input': input_data,
                    'expected_output': expected_output,
                    'actual_output': actual_output
                })

        return passed_test_cases, failed_test_cases