# Create your views here.
from oauth2_provider.ext.rest_framework import OAuth2Authentication
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from feedback_survey.filters import FeedbackStudentFilter

from feedback_survey.models import Feedback, Course, Teacher, Section, Student, SectionField
from feedback_survey.serializers import FeedbackSerializer, CourseSerializer, TeacherSerializer, SectionSerializer, \
    StudentSerializer, FeedbackCreateSerializer, StudentCreateSerializer, CourseCreateSerializer, \
    SectionCreateSerializer, SectionFieldSerializer
from feedback_survey.utils import CustomMetaDataMixin
from rest_framework import filters


class FeedbackSurveyViewSet(CustomMetaDataMixin, ModelViewSet):
    """

    """
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = FeedbackStudentFilter
    # authentication_classes = [OAuth2Authentication, ]
    # permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get_serializer_class(self):
        if self.is_create_api:
            return FeedbackCreateSerializer
        return FeedbackSerializer

    @property
    def is_create_api(self):
        return self.request.method == 'POST'


class CourseViewSet(CustomMetaDataMixin, ModelViewSet):
    """

    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # authentication_classes = [OAuth2Authentication, ]
    # permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get_serializer_class(self):
        if self.is_create_api:
            return CourseCreateSerializer
        return CourseSerializer

    @property
    def is_create_api(self):
        return self.request.method == 'POST'


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

    def get_serializer_class(self):
        if self.is_create_api:
            return SectionCreateSerializer
        return SectionSerializer

    @property
    def is_create_api(self):
        return self.request.method == 'POST'


class StudentSerializerViewSet(CustomMetaDataMixin, ModelViewSet):
    """
            Creating Student with course and university
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_serializer_class(self):
        if self.is_create_api:
            return StudentCreateSerializer
        return StudentSerializer

    @property
    def is_create_api(self):
        return self.request.method == 'POST'


class SectionFieldsSerializerViewSet(CustomMetaDataMixin, ModelViewSet):
    """

    """
    queryset = SectionField.objects.all()
    serializer_class = SectionFieldSerializer
