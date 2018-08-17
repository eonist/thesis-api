from rest_framework import generics, status
from rest_framework.response import Response

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

    def create(self, request, pk=None, company_pk=None, project_pk=None):
        is_many = True if isinstance(request.data, list) else False

        serializer = self.get_serializer(data=request.data, many=is_many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class TimeFrameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TimeFrame.objects.all()
    serializer_class = TimeFrameSerializer
