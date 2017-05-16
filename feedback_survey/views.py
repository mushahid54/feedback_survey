# Create your views here.
from oauth2_provider.ext.rest_framework import OAuth2Authentication
from rest_framework import permissions, generics
from rest_framework.viewsets import ModelViewSet
from feedback_survey.filters import FeedbackStudentFilter
from rest_framework.response import Response

from feedback_survey.models import Feedback, Course, Teacher, Section, Student, SectionField
from feedback_survey.serializers import FeedbackSerializer, CourseSerializer, TeacherSerializer, SectionSerializer, \
    StudentSerializer, FeedbackCreateSerializer, StudentCreateSerializer, CourseCreateSerializer, \
    SectionCreateSerializer, SectionFieldSerializer
from feedback_survey.utils import CustomMetaDataMixin
from rest_framework import filters


class FeedbackSurveyViewSet(CustomMetaDataMixin, ModelViewSet):
    """
        Added OAuth if wants just uncomment the authentication and permission class and make sure created access token
         at your end.
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


class StudentPendingFeedback(CustomMetaDataMixin, generics.RetrieveAPIView):
    """
        To get the value of the Student based on the

        1. **authentication:** yes
        2. **authorization:** authenticated user


    """
    # authentication_classes = [OAuth2Authentication, ]
    # permission_classes = [permissions.IsAuthenticated, ]

    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def retrieve(self, request, *args, **kwargs):
        student_id = self.request.query_params.get('student_id', None)
        instance = self.queryset.filter(state="1", student_id=student_id)
        serializer = self.get_serializer(instance, many=True)
        return Response(serializer.data)
