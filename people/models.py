# -*- coding: utf-8 -*-

from django.db import models
from universitytimetable.org.models import Department

class Person(models.Model):
    first_name = models.CharField(max_length=64, null=True, blank=True)
    middle_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64, null=True, blank=True)

    def __unicode__(self):
        return u'%s %s.%s.' % (
                self.last_name,
                self.first_name[0],
                self.middle_name[0],
                )


LECTURER_STATUS_CHOICES = (
        (u'ас.', u'асистент'),
        (u'ст. викл.', u'старший викладач'),
        (u'доц.', u'доцент'),
        (u'проф.', u'професор'),
        )


class LecturerStatus(models.Model):
    person = models.ForeignKey(Person)
    department = models.ForeignKey(Department, null=True, blank=True)
    status = models.CharField(max_length=255, choices=LECTURER_STATUS_CHOICES)
    date_from = models.DateField()
    date_to = models.DateField(null=True, blank=True)
