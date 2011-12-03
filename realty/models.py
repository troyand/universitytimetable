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
        if self.number:
            number_part = u'Корпус №%d' % self.number
        else:
            number_part = u''
        if self.label:
            label_part = self.label
        else:
            label_part = u''
        return u' - '.join([
                self.university.abbr,
                number_part,
                label_part,
                ])
