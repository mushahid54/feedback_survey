from rest_framework import serializers
from feedback_survey.models import Course, Teacher, FeedbackTemplate, SectionField, Section, Feedback, Student, \
    University


class UniversitySerializer(serializers.ModelSerializer):
    """

    """

    class Meta:
        model = University
        fields = ('name', 'address')


class CourseSerializer(serializers.ModelSerializer):
    """

    """
    university = UniversitySerializer()
    class Meta:
        model = Course
        fields = ('name', 'course_id', 'university')




class TeacherSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = Teacher
        fields = '__all__'


class SectionFieldSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = SectionField
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    """

    """
    course = serializers.SlugRelatedField(queryset=Course.objects.all(), many=True, slug_field="name")

    class Meta:
        model = Student
        fields = ('name', 'email', 'course')


class SectionSerializer(serializers.ModelSerializer):
    """
    """

    section_fields = SectionFieldSerializer(many=True)
    class Meta:
        model = Section
        fields = '__all__'

class FeedbackTemplateSerializer(serializers.ModelSerializer):
    """

    """
    sections = SectionSerializer(many=True)

    class Meta:
        model = FeedbackTemplate
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    """

    """
    student = StudentSerializer()
    course = serializers.CharField(source='course.name')

    class Meta:
        model = Feedback
        fields = ('id', 'course',  'student', 'rating')







