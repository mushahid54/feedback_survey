from rest_framework.test import APITestCase
from feedback_survey.models import Course, University, Student, FeedbackTemplate, Section, SectionField

__author__ = 'MushahidKhan'


class CreateFeedbackTestCase(APITestCase):
    def setUp(self):

        self.university = University.objects.create(name="Stanford", address="CA")
        self.course = Course.objects.create(name="Btech", course_id="BT01", university=self.university)
        self.student = Student.objects.create(name="James", email="abc@gmail.com",
                                              university=self.university)
        self.student.course.add(self.course)

        self.sectionfield = SectionField.objects.create(name="Hey", field_type="text", values="whatsup" )
        self.sections = Section.objects.create(name="Dream")
        self.sections.section_fields.add(self.sectionfield)

        self.feedback_template = FeedbackTemplate.objects.create(name="Question")
        self.feedback_template.sections.add(self.sections)

        self.request_json = {
            "course": self.course.id,
            "university": self.university.id,
            "rating": 5,
            "state": "1",
            "student": self.student.id,
            "feedback_template": self.feedback_template.id,

        }

    def test_create_order(self):
        """
             Test to get the feedback survey details
        :return:
        """
        response = self.client.post('/api/v1/feedback-survey/', data=self.request_json, format='json')

        self.assertEquals(response.status_code, 201)
