from django.contrib.postgres.fields import ArrayField
from django.db import models

from eeg_project.app.utils.config import GENDER_CHOICES


class Person(models.Model):
    created = models.DateTimeField(auto_now_add=True, )
    name = models.CharField(max_length=100, blank=False)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=100, blank=False)
    age = models.IntegerField(blank=False)

    class Meta:
        ordering = ('created',)


class Label(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created',)


class Session(models.Model):
    created = models.DateTimeField(auto_now_add=True, )
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='sessions', )
    ch_names = ArrayField(models.CharField(max_length=5), size=8, blank=False)
    real_data = models.BooleanField(default=False)

    @property
    def timeframe_count(self):
        return self.timeframes.count()

    @property
    def labels(self):
        if self.timeframes.count() == 0:
            return []

        label_ids = self.timeframes.values_list('label', flat=True)
        label_names = Label.objects.filter(id__in=label_ids).values_list('name', flat=True)
        return label_names

    class Meta:
        ordering = ('created',)


class TimeFrame(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='timeframes', )
    sensor_data = ArrayField(models.FloatField(), size=8, )
    label = models.ForeignKey(Label, on_delete=models.CASCADE, related_name='timeframes')
    timestamp = models.FloatField()

    class Meta:
        ordering = ('created',)
