import random

__author__ = 'Mushahid Khan'
from django.core.management.base import BaseCommand, CommandError
from feedback_survey.models import FeedbackTemplate, Section , SectionField


class SectionFieldTypes:
    TEXT = 'text'
    SUB_SECTION = 'sub_section'
    RADIO = 'yes_no_radio'


class Command(BaseCommand):
    help = "have to check this command not completed"

    def handle(self, *args, **options):
        # create five templates
        feedback_template_1 = FeedbackTemplate.objects.create(name='Feedback Template 1')
        self.populate_feedback_template_1(feedback_template_1)

        feedback_template_2 = FeedbackTemplate.objects.create(name='Feedback Template 2')
        self.populate_feedback_template_2(feedback_template_2)

        feedback_template_3 = FeedbackTemplate.objects.create(name='Feedback Template 3')
        self.populate_feedback_template_3(feedback_template_3)

        feedback_template_4 = FeedbackTemplate.objects.create(name='Feedback Template 4')
        self.populate_feedback_template_4(feedback_template_4)

        feedback_template_5 = FeedbackTemplate.objects.create(name='Feedback Template 5')
        self.populate_feedback_template_5(feedback_template_5)

    def create_section(self, name):
        return Section.objects.create(name="ABC")

    def populate_feedback_template_1(self, feedback_template_1):
        section_1 = self.create_section(name="Section 1")
        sub_section_a = SectionField.objects.create(name='SubSection A: Name', field_type=SectionFieldTypes.SUB_SECTION)
        name_field = SectionField.objects.create(name='Name: ', field_type=SectionFieldTypes.TEXT, parent_section=sub_section_a)

        sub_section_b = SectionField.objects.create(name='SubSection B: Contact Details', field_type=SectionFieldTypes.SUB_SECTION)
        email_field = SectionField.objects.create(name='Email: ', field_type=SectionFieldTypes.TEXT, parent_section=sub_section_b)
        phone_field = SectionField.objects.create(name='Phone: ', field_type=SectionFieldTypes.TEXT, parent_section=sub_section_b)

        # add sub_sections to section
        section_1.section_fields.add(*[sub_section_a, sub_section_b])

        section_2 = self.create_section(name="Section 2")
        sub_section_c = SectionField.objects.create(name='SubSection C: Feedback', field_type=SectionFieldTypes.SUB_SECTION)
        did_you_like_field = SectionField.objects.create(name='Did you like the Course?', field_type=SectionFieldTypes.RADIO, parent_section=sub_section_c)
        # add sub_sections to section
        section_2.section_fields.add(*[sub_section_c, ])

        # add sections to template
        feedback_template_1.sections.add(*[section_1, section_2])

    def populate_feedback_template_2(self, feedback_template_2):
        section_1 = self.create_section(name="Section 1")
        sub_section_a = SectionField.objects.create(name='SubSection A: Name', field_type=SectionFieldTypes.SUB_SECTION)
        name_field = SectionField.objects.create(name='Name: ', field_type=SectionFieldTypes.TEXT, parent_section=sub_section_a)
        email_field = SectionField.objects.create(name='Email: ', field_type=SectionFieldTypes.TEXT, parent_section=sub_section_a)
        phone_field = SectionField.objects.create(name='Phone: ', field_type=SectionFieldTypes.TEXT, parent_section=sub_section_a)
        # add sub_sections to section
        section_1.section_fields.add(*[sub_section_a,])

        # section 2
        section_2 = self.create_section(name="Section 2")
        sub_section_b = SectionField.objects.create(name='SubSection B: Feedback', field_type=SectionFieldTypes.SUB_SECTION)
        did_you_like_field = SectionField.objects.create(name='Did you like the Course?', field_type=SectionFieldTypes.RADIO, parent_section=sub_section_b)
        comments_field = SectionField.objects.create(name='Any Comments?', field_type=SectionFieldTypes.TEXT, parent_section=sub_section_b)
        # add sub_sections to section
    	section_2.section_fields.add(*[sub_section_b, ])

        # add sections to template
        feedback_template_2.sections.add(*[section_1, section_2])


    def populate_feedback_template_3(self, feedback_template_3):
        # section 1
        section_1 = self.create_section(name="Section 1")
        sub_section_a = SectionField.objects.create(name='SubSection A: Feedback', field_type=SectionFieldTypes.SUB_SECTION)
        did_you_like_field = SectionField.objects.create(name='Did you like the Course?', field_type=SectionFieldTypes.RADIO, parent_section=sub_section_a)
        comments_field = SectionField.objects.create(name='Any Comments?', field_type=SectionFieldTypes.TEXT, parent_section=sub_section_a)
        # add sub_sections to section
        section_1.section_fields.add(*[sub_section_a, ])

        # section 2
        section_2 = self.create_section(name="Section 2")
        sub_section_b = SectionField.objects.create(name='SubSection B: Details', field_type=SectionFieldTypes.SUB_SECTION)
        name_field = SectionField.objects.create(name='Name: ', field_type=SectionFieldTypes.TEXT, parent_section=sub_section_b)
        email_field = SectionField.objects.create(name='Email: ', field_type=SectionFieldTypes.TEXT, parent_section=sub_section_b)
        phone_field = SectionField.objects.create(name='Phone: ', field_type=SectionFieldTypes.TEXT, parent_section=sub_section_b)
        # add sub_sections to section
        section_2.section_fields.add(*[sub_section_b, ])

        # add sections to template
        feedback_template_3.sections.add(*[section_1, section_2])

    def populate_feedback_template_4(self, feedback_template_4):
        # section 1
        section_1 = self.create_section(name="Section 1")
        sub_section_a = SectionField.objects.create(name='SubSection A: Feedback', field_type=SectionFieldTypes.SUB_SECTION)
        did_you_like_field = SectionField.objects.create(name='Did you like the Course?', field_type=SectionFieldTypes.RADIO, parent_section=sub_section_a)
        # add sub_sections to section
    	section_1.section_fields.add(*[sub_section_a, ])

        # section 2
        section_2 = self.create_section(name="Section 2")
        sub_section_b = SectionField.objects.create(name='SubSection B: Name', field_type=SectionFieldTypes.SUB_SECTION)
        name_field = SectionField.objects.create(name='Name: ', field_type=SectionFieldTypes.TEXT, parent_section=sub_section_b)

        sub_section_c = SectionField.objects.create(name='SubSection C: Contact Details', field_type=SectionFieldTypes.SUB_SECTION)
        email_field = SectionField.objects.create(name='Email: ', field_type=SectionFieldTypes.TEXT, parent_section=sub_section_c)
        phone_field = SectionField.objects.create(name='Phone: ', field_type=SectionFieldTypes.TEXT, parent_section=sub_section_c)
        # add sub_sections to section
        section_2.section_fields.add(*[sub_section_b, sub_section_c])

        # add sections to template
        feedback_template_4.sections.add(*[section_1, section_2])


    def populate_feedback_template_5(self, feedback_template_5):

        # section 1
        section_1 = self.create_section(name="Section 1")
        sub_section_a = SectionField.objects.create(name='SubSection A: Feedback', field_type=SectionFieldTypes.SUB_SECTION)
        name_field = SectionField.objects.create(name='Name: ', field_type=SectionFieldTypes.TEXT, parent_section=sub_section_a)
        email_field = SectionField.objects.create(name='Email: ', field_type=SectionFieldTypes.TEXT, parent_section=sub_section_a)
        phone_field = SectionField.objects.create(name='Phone: ', field_type=SectionFieldTypes.TEXT, parent_section=sub_section_a)
        did_you_like_field = SectionField.objects.create(name='Did you like the Course?', field_type=SectionFieldTypes.RADIO, parent_section=sub_section_a)
        comments_field = SectionField.objects.create(name='Any Comments?', field_type=SectionFieldTypes.TEXT, parent_section=sub_section_a)
        # add sub_sections to section
        section_1.section_fields.add(*[sub_section_a, ])

        # add sections to template
        feedback_template_5.sections.add(*[section_1, ])