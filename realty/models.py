#-*- coding: utf-8 -*-

from django.db import models
from universitytimetable.org.models import University

class Building(models.Model):
    university = models.ForeignKey(University)
    number = models.IntegerField(null=True, blank=True)
    label = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        unique_together = ('university', 'number', 'label')

    def __unicode__(self):
        parts = [self.university.abbr]
        if self.number:
            parts.append(u'Корпус №%d' % self.number)
        if self.label:
            parts.append(self.label)
        return u' - '.join(parts)
