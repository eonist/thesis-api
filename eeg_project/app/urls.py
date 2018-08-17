from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from eeg_project.app import views

urlpatterns = [
    url(r'^persons$', views.PersonList.as_view()),
    url(r'^persons/(?P<pk>[0-9]+)/$', views.PersonDetail.as_view()),
    url(r'^sessions$', views.SessionList.as_view()),
    url(r'^sessions/(?P<pk>[0-9]+)/$', views.SessionDetail.as_view()),
    url(r'^time-frames$', views.TimeFrameList.as_view()),
    url(r'^time-frames/(?P<pk>[0-9]+)/$', views.TimeFrameDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
