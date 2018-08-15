from rest_framework import generics

from eeg_project.app.models import Person, Session, TimeFrame
from eeg_project.app.serializers import PersonSerializer, SessionSerializer, TimeFrameSerializer


class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class SessionList(generics.ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class SessionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class TimeFrameList(generics.ListCreateAPIView):
    queryset = TimeFrame.objects.all()
    serializer_class = TimeFrameSerializer


class TimeFrameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TimeFrame.objects.all()
    serializer_class = TimeFrameSerializer
