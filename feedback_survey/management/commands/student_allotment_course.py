__author__ = 'Mushahid Khan'
from django.core.management.base import BaseCommand, CommandError
from feedback_survey.models import Course, Student, University

class Command(BaseCommand):

    help = "Creating Student based on the courses "

    def handle(self, *args, **options):
        course_one = Course.objects.get_or_create(name="Btech", course_id="BT1")
        course_one = Course.objects.get_or_create(name="BSc", course_id="BS1")
        course_one = Course.objects.get_or_create(name="BCom", course_id="BC1")
        university = University.objects.create(name="Stanford")
        course_list = Course.objects.all()

        student_name_list = ["Stud@"+`i` for i in range(300)]
        for student_name in student_name_list:
            for course in course_list:
                Student.objects.get_or_create(course=course, university=university, name=student_name, email="abc@gmail.com")
        return
