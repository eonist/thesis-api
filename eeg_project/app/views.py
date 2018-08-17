from rest_framework import generics, status
from rest_framework.response import Response

from eeg_project.app.models import Person, Session, TimeFrame
from eeg_project.app.serializers import PersonSerializer, SessionSerializer, TimeFrameSerializer


class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def post(self, request, *args, **kwargs):
        person, created = \
            Person.objects.get_or_create(name=request.data["name"], age=request.data["age"],
                                         gender=request.data["gender"])

        serializer = PersonSerializer(person)
        headers = self.get_success_headers(serializer.data)

        if created:
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class SessionList(generics.ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    def get_queryset(self):
        queryset = Session.objects.all()
        person_id = self.request.query_params.get('person', None)
        if person_id is not None:
            queryset = queryset.filter(person=person_id)
        return queryset


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
