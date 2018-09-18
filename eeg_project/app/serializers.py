from rest_framework import serializers

from eeg_project.app.models import Person, Session, TimeFrame, Label


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class SessionSerializer(serializers.ModelSerializer):
    timeframe_count = serializers.ReadOnlyField()
    labels = serializers.ReadOnlyField()

    class Meta:
        model = Session
        fields = '__all__'


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = '__all__'


class TimeFrameSerializer(serializers.ModelSerializer):
    label = LabelSerializer(read_only=True)
    label_id = serializers.PrimaryKeyRelatedField(source='label', queryset=Label.objects.all(), write_only=True)

    class Meta:
        model = TimeFrame
        fields = ('id', 'session', 'label', 'label_id', 'sensor_data', 'created', 'timestamp')
