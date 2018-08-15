from rest_framework import serializers

from eeg_project.app.models import Person, Session, TimeFrame


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'name', 'gender', 'age')


class SessionSerializer(serializers.ModelSerializer):
    time_frames = serializers.StringRelatedField(many=True)
    person = PersonSerializer(required=True)

    class Meta:
        model = Session
        fields = ('id', 'person', 'time_frames', 'person')


class TimeFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeFrame
        fields = ('id', 'sensor_data', 'label', 'session')
