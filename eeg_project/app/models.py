from django.contrib.postgres.fields import ArrayField
from django.db import models

from eeg_project.app.utils.config import GENDER_CHOICES


class Person(models.Model):
    created = models.DateTimeField(auto_now_add=True, )
    name = models.CharField(max_length=100, blank=False, default='', )
    gender = models.CharField(choices=GENDER_CHOICES, max_length=100, default="male")
    age = models.IntegerField(default=24)

    class Meta:
        ordering = ('created',)


class Session(models.Model):
    created = models.DateTimeField(auto_now_add=True, )
    person = models.OneToOneField(Person, on_delete=models.CASCADE, )

    class Meta:
        ordering = ('created',)


class TimeFrame(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='time_frames', )
    sensor_data = ArrayField(models.FloatField(), size=8, )
    label = ArrayField(models.FloatField(), size=2, )

    class Meta:
        ordering = ('created',)
