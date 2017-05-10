
import random

__author__ = 'Mushahid Khan'
from django.core.management.base import BaseCommand, CommandError
from feedback_survey.models import Student, Feedback, FeedbackTemplate


class Command(BaseCommand):

    help = "Creating Student based on the courses"

    def handle(self, *args, **options):
        for student in Student.objects.all():
            for course in student.course.all():
                feedback_template_ids = list(FeedbackTemplate.objects.all().values_list('id', flat=True))
                random_feedback_template = random.choice(feedback_template_ids)
                fb_template_obj = FeedbackTemplate.objects.get(id=random_feedback_template)
                feedback_object = Feedback.objects.create(student=student, course=course, rating=0, feedback_template=fb_template_obj)


        return



