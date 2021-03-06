
from django.db import models
from django.db.models import Avg


STATUS_CHOICES = (
    ('1', 'Pending'),
    ('2', 'Completed')
)

class Teacher(models.Model):
    """
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Course(models.Model):
    """
    Courses which are provided by University.
    """
    name = models.CharField(max_length=50)
    course_id = models.CharField(max_length=10)
    teacher = models.ForeignKey("feedback_survey.Teacher", null=True, blank=True)
    university = models.ForeignKey("feedback_survey.University", null=True, blank=True)

    def __str__(self):
        return self.name

    def get_university(self):
        if self.university:
            return self.university.name
        else:
            return "N/A"

    @property
    def course_avg_rating(self):
        avg_rating = Feedback.objects.filter(course=self).aggregate(Avg('rating'))['rating__avg']

        return avg_rating

    def get_student_attached_to_course(self):
        return "\n".join([student.name for student in self.student_set.all()])


class SectionField(models.Model):
    """
    """
    name = models.CharField(max_length=50)
    field_type = models.CharField(max_length=20)
    values = models.CharField(max_length=50)
    parent_section = models.ForeignKey("self", null=True, blank=True)


class Section(models.Model):
    """
    """
    name = models.CharField(max_length=50)
    section_fields = models.ManyToManyField("feedback_survey.SectionField")

    def __str__(self):
       return self.name

    def get_products(self):
        return "\n".join([p.name for p in self.section_fields.all()])


class FeedbackTemplate(models.Model):
    """
    """
    name = models.CharField(max_length=50, blank=True)
    sections = models.ManyToManyField("feedback_survey.Section")

    def __str__(self):
        return str(self.id)

    def get_sections(self):
        return "\n".join([p.name for p in self.sections.all()])


class Feedback(models.Model):
    """
    """
    course = models.ForeignKey("feedback_survey.Course", null=True, blank=True)
    student = models.ForeignKey("feedback_survey.Student", null=True, blank=True)
    rating = models.IntegerField()
    state = models.CharField(max_length=3, choices=STATUS_CHOICES, default=1)
    feedback_template = models.ForeignKey("feedback_survey.FeedbackTemplate", null=True, blank=True)

    def __str__(self):
        return self.course.name


class University(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=200)

    def __str__(self):
        return self.name


class Student(models.Model):
    """
        Each Student belong to at least one course and one university
    """
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=255, blank=True)
    course = models.ManyToManyField("feedback_survey.Course", blank=True)
    university = models.ForeignKey("feedback_survey.University", blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_university(self):
        if self.university:
            return self.university.name
        else:
            return "N/A"

    def get_course(self):
        if self.course:
            return "\n".join([student_course.name for student_course in self.course.all()])
        else:
            return "N/A"



