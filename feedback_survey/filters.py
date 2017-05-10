import django_filters
from rest_framework import filters
from feedback_survey.models import Feedback

__author__ = 'Mushahid Khan'


class FeedbackStudentFilter(filters.FilterSet):
    student_id = django_filters.CharFilter(name="student_id")

    class Meta:
        model = Feedback
        fields = ('student_id',)
