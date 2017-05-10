

from django.contrib import admin
from feedback_survey.models import Course, SectionField, Feedback, FeedbackTemplate, Teacher, University, Student, \
    Section


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'course_id', 'course_avg_rating', 'get_university')

admin.site.register(Course, CourseAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'get_university', 'get_course')

admin.site.register(Student, StudentAdmin)


class UniversityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address')

admin.site.register(University, UniversityAdmin)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('course', 'rating', 'student')

admin.site.register(Feedback, FeedbackAdmin)


class SectionFieldAdmin(admin.ModelAdmin):
    list_display = ('name', 'field_type')

admin.site.register(SectionField, SectionFieldAdmin)



class FeedbackTemplateAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_sections')

admin.site.register(FeedbackTemplate, FeedbackTemplateAdmin)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Teacher, TeacherAdmin)


class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_products')

admin.site.register(Section, SectionAdmin)

