from django.shortcuts import get_object_or_404, render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from . import parsers
from .models import Lesson, Step, StepUser
from .serializers import LessonSerializer, StepSerializer, StepUserSerializer


class LessonsDetail(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'


class StepDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, lesson_id, number, format=None):
        """
        By this view user can see the detail of current step.
        :lesson_id - id of current course.
        :id - id of current step.
        """
        step = get_object_or_404(Step, lesson_id=lesson_id, number=number)
        if step:
            serializer = StepSerializer(step)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, lesson_id, number, format=None):
        try:
            request_test = parsers.parse_test(request.data)
            request_tasks = parsers.parse_tasks(request.data)
            posted_cases = parsers.parse_cases(request.data)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        step = Step.get_by_lesson_id_and_numebr(lesson_id, number)

        stepuser_instance = StepUser.create_stepuser(
            user=request.user,
            step=step,
            passed=request_test.is_passed(request_tasks, posted_cases),
            score=request_test.passed_count(
                request_tasks)*len(request_tasks)*100
        )

        stepuser_serializer = StepUserSerializer(stepuser_instance)
        return Response(stepuser_serializer.data, status=status.HTTP_201_CREATED)

    