from datetime import timezone
from django.db import models


class Teacher(models.Model):
    """
    """
    name = models.CharField(max_length=50)


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

    @property
    def course_avg_rating(self):
        course_feedbacks = Feedback.objects.filter(course=self)
        courses = len(course_feedbacks)
        rating_count = 0
        avg_rating = 0
        for course in course_feedbacks:
            rating_count += course.rating
        try:
            avg_rating = rating_count / courses
        except ZeroDivisionError:
            pass
        return avg_rating

    def get_university(self):
        if self.university:
            return self.university.name
        else:
            return "N/A"


class SectionField(models.Model):
    """
    """
    name = models.CharField(max_length=50)
    field_type = models.CharField(max_length=20)
    values = models.CharField(max_length=50)
    nested_section = models.ForeignKey("self", null=True, blank=True)


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

    sections = models.ManyToManyField("feedback_survey.Section")

    def __str__(self):
        return str(self.id)

    def get_sections(self):
        return "\n".join([p.name for p in self.sections.all()])


class Feedback(models.Model):
    """
    """
    course = models.ForeignKey("feedback_survey.Course", null=True, blank=True)
    rating = models.IntegerField()
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
    name = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=255, blank=True)
    course = models.ForeignKey("feedback_survey.Course", blank=True)
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
            return self.course.name
        else:
            return "N/A"



