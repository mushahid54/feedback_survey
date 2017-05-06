from django.shortcuts import render

# Create your views here.
from oauth2_provider.ext.rest_framework import OAuth2Authentication
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from feedback_survey.models import Feedback, Course, Teacher, Section, Student
from feedback_survey.serializers import FeedbackSerializer, CourseSerializer, TeacherSerializer, SectionSerializer, \
    StudentSerializer
from feedback_survey.utils import CustomMetaDataMixin


class FeedbackSurveyViewSet(CustomMetaDataMixin, ModelViewSet):
    """

    """
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    # authentication_classes = [OAuth2Authentication, ]
    # permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class CourseViewSet(CustomMetaDataMixin, ModelViewSet):
    """

    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # authentication_classes = [OAuth2Authentication, ]
    # permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class TeacherSerializerViewSet(CustomMetaDataMixin, ModelViewSet):
    """

    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    # authentication_classes = [OAuth2Authentication, ]
    # permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class SectionSerializerViewSet(CustomMetaDataMixin, ModelViewSet):
    """

    """
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class StudentSerializerViewSet(CustomMetaDataMixin, ModelViewSet):
    """

    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
