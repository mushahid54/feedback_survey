from django.conf.urls import url
from feedback_survey.views import StudentPendingFeedback

urlpatterns = [


    url(r'^student-pending-feedback/$', StudentPendingFeedback.as_view(), name='get_coupon_value')




]

