"""paysensetask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

from authentication.views import UserViewSet
#from chatapp.views import ChatMessageViewSet
from feedback_survey.views import FeedbackSurveyViewSet, CourseViewSet, TeacherSerializerViewSet, \
    SectionSerializerViewSet, StudentSerializerViewSet, SectionFieldsSerializerViewSet

router = routers.DefaultRouter()
#router.register(r'chat-messages', ChatMessageViewSet)
router.register(r'create-user', UserViewSet)
router.register(r'students', StudentSerializerViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'feedback-survey', FeedbackSurveyViewSet)
router.register(r'teachers', TeacherSerializerViewSet)
router.register(r'sections', SectionSerializerViewSet)
router.register(r'sections-fields', SectionFieldsSerializerViewSet)


schema_view = get_swagger_view(title='Feedback Survey API')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^api/v1/', include(router.urls, namespace='api')),
    url(r'^$', schema_view),
    url(r'^api/v1/', include('feedback_survey.urls', namespace='feedback_survey')),
]
