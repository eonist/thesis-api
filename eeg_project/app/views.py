from rest_framework import generics, status
from rest_framework.response import Response

from eeg_project.app.models import Person, Session, TimeFrame, Label
from eeg_project.app.serializers import PersonSerializer, SessionSerializer, TimeFrameSerializer, LabelSerializer
from eeg_project.app.utils.config import LABEL_MAP
from eeg_project.app.utils.utils import is_number


class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def post(self, request, *args, **kwargs):
        person, created = \
            Person.objects.get_or_create(**request.data)

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

        is_real_data = self.request.query_params.get('real', None)
        if is_real_data is not None:
            queryset = queryset.filter(is_real_data=is_real_data)

        return queryset


class SessionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class TimeFrameList(generics.ListCreateAPIView):
    queryset = TimeFrame.objects.all()
    serializer_class = TimeFrameSerializer

    def create(self, request, pk=None, company_pk=None, project_pk=None):
        if not isinstance(request.data, list):
            raise Exception("TimeFrameList Create expected a list as request data")

        for i in range(len(request.data)):
            if not is_number(request.data[i]["label"]):
                label, created = Label.objects.get_or_create(name=request.data[i]["label"])
                request.data[i]["label_id"] = label.id

        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        queryset = TimeFrame.objects.all()
        session_id = self.request.query_params.get('session', None)
        if session_id is not None:
            queryset = queryset.filter(session=session_id)
        return queryset


class TimeFrameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TimeFrame.objects.all()
    serializer_class = TimeFrameSerializer


class LabelList(generics.ListCreateAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer

    def post(self, request, *args, **kwargs):
        name = request.data["name"]
        if name in LABEL_MAP:
            value = LABEL_MAP[name]
            label, created = Label.objects.get_or_create(name=name, value=value)
        else:
            label, created = Label.objects.get_or_create(name=name)

        if "value" in request.data:
            label.value = request.data["value"]

        serializer = LabelSerializer(label)
        headers = self.get_success_headers(serializer.data)

        if created:
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)


class LabelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
